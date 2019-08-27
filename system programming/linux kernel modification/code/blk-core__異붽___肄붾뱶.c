/*
	�ۼ���: ������ (����: ���ذ�)
	�ۼ���: 2017.11.3(�ϼ��� ����)
*/

/*
	blk-core.c line 2095�� �߰�
	CQ_BUF_HEAD, CQ_BUF_TAIL, CQ_length, CQ: lkm���� 
	Queue�� ���� ������ ������ �� �ֵ��� EXPORT_SYMBOL ó��
	ť�� ��ȯ�� �� �ֵ��� �����Ͽ���.
	submit_bio �Լ� ���� rw & WRITE �Ӽ��� true�� ��쿡 CQ_enque�� ȣ���Ͽ� block_number, tm �� ����
*/

#define CQ_BUF_SIZE 16384
int CQ_BUF_HEAD = 0;
int CQ_BUF_TAIL = -1;
int CQ_length = 0;
struct bnotime CQ[CQ_BUF_SIZE];

EXPORT_SYMBOL(CQ_BUF_HEAD);
EXPORT_SYMBOL(CQ_BUF_TAIL);
EXPORT_SYMBOL(CQ_length);
EXPORT_SYMBOL(CQ);
struct bnotime CQ_deque(void);
void CQ_enque(unsigned long long bn, struct tm *t, struct bio **blockio)
{
	if (CQ_BUF_HEAD == (CQ_BUF_TAIL + 1) % CQ_BUF_SIZE && CQ_length > 0)
	{
		CQ_BUF_HEAD = (CQ_BUF_HEAD + 1) % CQ_BUF_SIZE;
		CQ_length--;
	}
	CQ_BUF_TAIL = (CQ_BUF_TAIL + 1) % CQ_BUF_SIZE;
	CQ[CQ_BUF_TAIL].block_number = bn;
	CQ[CQ_BUF_TAIL].hour = t->tm_hour;
	CQ[CQ_BUF_TAIL].min = t->tm_min;
	CQ[CQ_BUF_TAIL].sec = t->tm_sec;
	CQ[CQ_BUF_TAIL].bio = blockio;
	CQ[CQ_BUF_TAIL].bdev = NULL;
	CQ[CQ_BUF_TAIL].bdev = (*blockio)->bi_bdev;

	CQ_length++;
}
struct bnotime CQ_deque(void)
{
	if (CQ_length <= 0)
	{
		struct bnotime temp;
		CQ_length = 0;
		return temp;
	}
	struct bnotime result = CQ[CQ_BUF_HEAD];
	CQ_BUF_HEAD = (CQ_BUF_HEAD + 1) % CQ_BUF_SIZE;
	CQ_length--;
	return result;
}

blk_qc_t submit_bio(int rw, struct bio *bio)
{
	bio->bi_rw |= rw;
	struct timeval time;
	/*
	* If it's a regular read/write or a barrier with data attached,
	* go through the normal accounting stuff before submission.
	*/
	if (bio_has_data(bio)) {
		unsigned int count;

		if (unlikely(rw & REQ_WRITE_SAME))
			count = bdev_logical_block_size(bio->bi_bdev) >> 9;
		else
			count = bio_sectors(bio);

		if (rw & WRITE) {
			struct tm broken;
			do_gettimeofday(&time);
			time_to_tm(time.tv_sec, 0, &broken);
			CQ_enque((unsigned long long)bio->bi_iter.bi_sector, &broken, &bio);
			count_vm_events(PGPGOUT, count);
		}
		else {
			task_io_account_read(bio->bi_iter.bi_size);
			count_vm_events(PGPGIN, count);
		}

		if (unlikely(block_dump)) {
			char b[BDEVNAME_SIZE];
			printk(KERN_DEBUG "%s(%d): %s block %Lu on %s (%u sectors)\n",
				current->comm, task_pid_nr(current),
				(rw & WRITE) ? "WRITE" : "READ",
				(unsigned long long)bio->bi_iter.bi_sector,
				bdevname(bio->bi_bdev, b),
				count);
		}
	}

	return generic_make_request(bio);
}
EXPORT_SYMBOL(submit_bio);