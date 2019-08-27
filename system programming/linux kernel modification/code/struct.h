/*
	작성자: 이태현
	작성일: 2017.11.3
*/

struct bnotime{
		unsigned long long block_number;
		struct tm *time;
		struct bio **bio;
		int hour;
		int min;
		int sec;

		char **name;
		char sysname[100];
		struct block_device *bdev;
};
#define Q_BUF_SIZE 1024
