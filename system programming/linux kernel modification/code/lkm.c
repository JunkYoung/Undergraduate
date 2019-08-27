/*
	작성자 : 이태현, 이준경
	작성일 : 2017.11.3
*/

/*
	lkm_print_buffer : CQ의 내용들을 출력
		CQ에 저장되어있는 bdev에서 get_super 함수를 통해 super_block을 가져온다. super_block 내 s_type->name에 접근하여 파일 시스템의 이름을 출력하게 된다.
		Enque시 저장해주었던 block number를 출력.
		각 구조체에 존재하는 hour, min, sec의 정보를 출력.
*/

#include <linux/module.h>
#include <linux/init.h>
#include <linux/kernel.h>
#include <linux/proc_fs.h>
#include <linux/struct.h>

#define MODULE_NAME "block_print"
#define BLOCK_FILE "blockprint"
#define BLOCK_DIR "block_print"
#define CQ_BUF_SIZE 16384

static struct proc_dir_entry *lkm_proc_dir, *lkm_proc_file;


extern int CQ_BUF_HEAD;
extern int CQ_BUF_TAIL;
extern struct bnotime CQ[CQ_BUF_SIZE];
extern int CQ_length;
static void lkm_print_buffer(void);
static ssize_t read_lkm_print_buffer(struct file * file, char __user * _user_bufffer, size_t ss, loff_t * looo)
{
	printk(KERN_INFO "readlkm\n");
	lkm_print_buffer();
	return 0;
}

static int open_lkm_print_buffer(struct inode * inode, struct file * file)
{
	printk(KERN_INFO "openlkm\n");
	lkm_print_buffer();
	return 0;
}

static void lkm_print_buffer(void)
{
	printk(KERN_INFO"lkm_print_buffer\n");
	int index = 0;
	int i = 0;
	//char bdbd[20];
	//printk(KERN_INFO "CQ_length : %d\n", CQ_length);
	//printk(KERN_INFO "CQ_BUF_HEAD : %d\n", CQ_BUF_HEAD);
	//printk(KERN_INFO "CQ_BUF_TAIL : %d\n", CQ_BUF_TAIL);
	for(i = CQ_BUF_HEAD; i != CQ_BUF_TAIL; i = (i + 1) % CQ_BUF_SIZE)
	{
		index = i;
		//printk(KERN_INFO "i : %d\n", i);
		//index = (CQ_BUF_HEAD + i) % CQ_BUF_SIZE;
		//printk(KERN_INFO "index : %d\nCQ_BUF_HEAD : %d\n",
		//			 index,
		//			 CQ_BUF_HEAD);
		
		/*
		printk(KERN_INFO "%10s\t%10llu\t%2d:%2d:%2d\n", 
				CQ[index].bio->bi_bdev->bd_super->s_id, 
				CQ[index].bio->bi_iter.bi_sector, 
				CQ[index].time->tm_hour, 
				CQ[index].time->tm_min, 
				CQ[index].time->tm_sec);
				*/
			struct bnotime temp = CQ[index];
			//if(get_super(temp.bdev) == NULL)
			// printk(KERN_INFO "fs: %5s\t", temp.bdev->bd_super->s_type->name);
			if (strcmp(get_super(temp.bdev)->s_type->name, "nilfs2") == 0) {
				printk(KERN_INFO "fs: %5s\t", get_super(temp.bdev)->s_type->name);
				printk(KERN_INFO "b_no : %10llu %2d:%2d:%2d\n", 
					temp.block_number,
					temp.hour,
					temp.min,
					temp.sec);
}
			//bdevname(temp.bdev, bdbd);
			//printk(KERN_INFO "bdev : %s\n", bdbd);
	}
}

static const struct file_operations myproc_fops = {
	.owner = THIS_MODULE,
	.open = open_lkm_print_buffer,
	.read = read_lkm_print_buffer,
};

static int lkm_init(void)
{
	printk(KERN_INFO "lkm online\n");
	lkm_proc_dir = proc_mkdir(BLOCK_DIR, NULL);
	printk(KERN_INFO "lkm_pro_dir set\n");
	if(lkm_proc_dir == NULL)
	{
		printk(KERN_INFO "mkdir failure\n");
		goto fail_entry;
	}
	printk(KERN_INFO"lkm_proc_file init\n");
	lkm_proc_file = proc_create(BLOCK_FILE, 0600, lkm_proc_dir, &myproc_fops);
	printk(KERN_INFO"lkm_proc_file init done\n");
	if(lkm_proc_file == NULL)
	{
		printk(KERN_INFO "read entry failure\n");
		goto fail_file;
	}
	return 0;
fail_entry:
	return 0;
fail_file:
	remove_proc_entry(MODULE_NAME, NULL);
	return 0;
}


static int lkm_exit(void)
{
	printk(KERN_INFO "lkm offline\n");
	remove_proc_entry(BLOCK_FILE, lkm_proc_file);
	remove_proc_entry(BLOCK_DIR, lkm_proc_dir);
	return 0;
}

module_init(lkm_init);
module_exit(lkm_exit);
MODULE_AUTHOR("LEE TAE HYUN");
MODULE_DESCRIPTION("PRINT BLOCK NUMBER");
MODULE_LICENSE("GPL");
MODULE_VERSION("1.0");
