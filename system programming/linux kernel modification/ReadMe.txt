
segbuf.c 는 /usr/src/linux-4.4/fs/nilfs2 안에 넣어줍니다.

struct.h 는 /usr/src/linux-4.4/include/linux 안에 넣어줍니다.

blk-core.c 는 /usr/src/linux-4.4/block 안에 넣어줍니다. 

blk-core 수정한 내용.c 는 수정한 코드만을 발췌하여 주석으로 설명해놓은 파일입니다.

lkm.c 는 lkm 소스파일입니다.

Makefile 은 lkm.c와 동일한 디렉토리에 위치하여 make 명령을 통해 컴파일 해줍니다.

lkm.ko는 Makefile을 통해 컴파일된 커널모듈입니다. 