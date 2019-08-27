#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct process_t {
	int process_ID;
	int CPU_burstT;
	int IO_burstT;
	int arrivalT;
	int priority;
	int turnaroundT;
	int waittingT;
} process;

#define Qsize 20
#define Psize 20

typedef struct readyQ_t {
	process p[Qsize];
	int front, rear;
} readyQ;

void Create_Process(process[], int);
void Schedule(int, process[], int, float[]);
int FCFS(process[], int);
int SJF_NP(process[], int);
int SJF_P(process[], int);
int Priority_NP(process[], int);
int Priority_P(process[], int);
int RR(process[], int);
void reset(process[], int);
void sort_arrival(readyQ*);
void insertQ(readyQ*, process[], int, int);
void sort_burst(readyQ[]);
void sort_priority(readyQ[]);
void Evaluation(process[], int, float[]);
void print_table(process[], int);
int first_arrival(process[], int);
void printChart();


int main() {
	int sel;
	int num;
	float result[12];

	process p[Psize];
	printf("\nCPUscheduling simulator\n");
	printf("\ninput number of process: ");
	scanf("%d", &num);

	Create_Process(p, num);
	printf("\n             ID   AT   BT   PR");
	for (int i = 0; i < num; i++) {
		printf("\nProcess %d: %4d %4d %4d %4d", i, p[i].process_ID, p[i].arrivalT, p[i].CPU_burstT, p[i].priority);
	}
	do {
		sel = 0;
		printf("\n\n1.FCFS\n2.SJF_NP\n3.SJF_P\n4.Priority_NP\n5.Priority_P\n6.RR\n7.Compare all\n\nselection: ");
		scanf("%d", &sel);
		Schedule(sel, p, num, result);
	} while (1);
	

	return 0;
}

void Create_Process(process p[], int num) {
	srand((unsigned)time(NULL));
	for (int i = 0; i < num; i++) {
		p[i].arrivalT = rand() % 30;
		p[i].CPU_burstT = rand() % 30 + 1;
		p[i].IO_burstT = rand() % 10 + 1;
		p[i].priority = rand() % 20;
		p[i].process_ID = i;
	}
}

void Schedule(int sel, process p[], int num, float result[]) {
	int res = 0;
	int c = 0;
	switch (sel) {
	case 1: {
		reset(p, num);
		res = FCFS(p, num);
		print_table(p, num);
		Evaluation(p, num, result);
		break;
	}
	case 2: {
		
		reset(p, num);
		res = SJF_NP(p, num);
		print_table(p, num);
		Evaluation(p, num, result);
		break;
	}
	case 3: {
		reset(p, num);
		res = SJF_P(p, num);
		print_table(p, num);
		Evaluation(p, num, result);
		break;
	}
	case 4: {
		reset(p, num);
		res = Priority_NP(p, num);
		print_table(p, num);
		Evaluation(p, num, result);
		break;
	}
	case 5: {
		reset(p, num);
		res = Priority_P(p, num);
		print_table(p, num);
		Evaluation(p, num, result);
		break;
	}
	case 6: {
		reset(p, num);
		res = RR(p, num);
		print_table(p, num);
		Evaluation(p, num, result);
		break;
	}
	case 7: {
		int j = 0;
		printf("\n\nCompare All\n");
		for (int i = 0; i < 12; i++) {
			result[i] = 0;
		}
		reset(p, num);
		Schedule(1, p, num, result);
		reset(p, num);
		Schedule(2, p, num, result);
		reset(p, num);
		Schedule(3, p, num, result);
		reset(p, num);
		Schedule(4, p, num, result);
		reset(p, num);
		Schedule(5, p, num, result);
		reset(p, num);
		Schedule(6, p, num, result);
		printf("\n    avg_TAT  avg_WT\n");
		for (int i = 0; i < 12; i = i + 2) {
			j++;
			printf("%d %4f %4f\n", j, result[i], result[i + 1]);
		}
	}
	}
}

int FCFS(process p[], int num) {
	printf("\n\nFCFS\n\n");
	int time = 0;

	readyQ rq;
	rq.front = rq.rear = 0;

	for (int i = 0; i < num; i++) {
		rq.rear = i;
		rq.p[i] = p[i];
	}

	sort_arrival(&rq);

	p[rq.p[rq.front].process_ID].turnaroundT = p[rq.p[rq.front].process_ID].CPU_burstT;
	p[rq.p[rq.front].process_ID].waittingT = 0;
	time = p[rq.p[rq.front].process_ID].arrivalT + p[rq.p[rq.front].process_ID].CPU_burstT;
	for (int i = 0; i < p[rq.p[rq.front].process_ID].arrivalT; i++)
		printf(". ");
	for (int i = p[rq.p[rq.front].process_ID].arrivalT; i < time; i++)
		printf("%d ", rq.p[rq.front].process_ID);
	for (int i = rq.front + 1; i <= rq.rear; i++) {
		if (time < p[rq.p[i].process_ID].arrivalT) {
			p[rq.p[i].process_ID].waittingT = 0;
			for (int j = time; j < p[rq.p[i].process_ID].arrivalT; j++)
				printf(". ");
			time = p[rq.p[i].process_ID].arrivalT;
		}
		else {
			p[rq.p[i].process_ID].waittingT = time - p[rq.p[i].process_ID].arrivalT;
		}
		p[rq.p[i].process_ID].turnaroundT = p[rq.p[i].process_ID].waittingT + p[rq.p[i].process_ID].CPU_burstT;
		time += p[rq.p[i].process_ID].CPU_burstT;
		for (int j = time - p[rq.p[i].process_ID].CPU_burstT; j < time; j++)
			printf("%d ", rq.p[i].process_ID);
	}
	printChart();

	return 0;
}

int SJF_NP(process p[], int num) {
	printf("\n\nSJF_NP\n\n");
	int time = 0;
	int done = 0;
	int exclude[10];

	for (int i = 0; i < 10; i++) {
		exclude[i] = 0;
	}

	int first = 0;
	
	while(done < num) {
		int minCPU = 99;
		for (int i = 0; i < num; i++) {
			if (time >= p[i].arrivalT && exclude[i] != 1) {
				if (p[i].CPU_burstT < minCPU) {
					minCPU = p[i].CPU_burstT;
					first = i;
				}
			}
		}
		if (minCPU == 99) {
			time++;
			printf(". ");	
		}
		else {
			for (int i = 0; i < p[first].CPU_burstT; i++) {
				printf("%d ", p[first].process_ID);
			}
			exclude[first] = 1;
			p[first].waittingT = time - p[first].arrivalT;
			time += p[first].CPU_burstT;
			p[first].turnaroundT = time - p[first].arrivalT;
			done++;
		}
	}
	printChart();

	return 0;
}

int SJF_P(process p[], int num) {
	printf("\n\nSJF_P\n\n");
	int done = 0;
	int time = 0;
	readyQ rq;
	for (int i = 0; i < Qsize; i++) {
		rq.p[i].process_ID = -1;
		rq.p[i].CPU_burstT = 0;
	}
	rq.front = 0;
	rq.rear = -1;

	while (done < num) {
		for (int i = 0; i < num; i++) {
			if (p[i].arrivalT == time) {
				insertQ(&rq, p, time, num);
				sort_burst(&rq);
			}
		}
		if (rq.front <= rq.rear) {
			printf("%d ", rq.p[rq.front].process_ID);
			rq.p[rq.front].CPU_burstT--;
			sort_burst(&rq);
		}
		else {
			printf(". ");
		}
		if (rq.p[rq.front].CPU_burstT == 0) {
			p[rq.p[rq.front].process_ID].turnaroundT = time - p[rq.p[rq.front].process_ID].arrivalT+1;
			p[rq.p[rq.front].process_ID].waittingT = p[rq.p[rq.front].process_ID].turnaroundT - p[rq.p[rq.front].process_ID].CPU_burstT; 
			done++;
			rq.front++;
		}
		time++;
	}
	printChart();

	return 0;
}

int Priority_NP(process p[], int num) {
	printf("\n\nPriority_NP\n\n");

	int time = 0;
	int done = 0;
	int exclude[10];
	for (int i = 0; i < 10; i++) {
		exclude[i] = 0;
	}
	int first = 0;

	while(done < num) {
		int minPri = 99;
		for (int i = 0; i < num; i++) {
			if (time >= p[i].arrivalT && exclude[i] != 1) {
				if (p[i].priority < minPri) {
					minPri = p[i].priority;
					first = i;
				}
			}
		}
		if (minPri == 99) {
			time++;
			printf(". ");	
		}
		else {
			for (int i = 0; i < p[first].CPU_burstT; i++) {
				printf("%d ", p[first].process_ID);
			}
			exclude[first] = 1;
			p[first].waittingT = time - p[first].arrivalT;
			time += p[first].CPU_burstT;
			p[first].turnaroundT = time - p[first].arrivalT;
			done++;
		}
	}
	printChart();

	return 0;
}

int Priority_P(process p[], int num) {
	printf("\n\nPriority_P\n\n");
	int done = 0;
	int time = 0;
	readyQ rq;
	for (int i = 0; i < Qsize; i++) {
		rq.p[i].process_ID = -1;
		rq.p[i].CPU_burstT = -1;
	}
	rq.front = 0;
	rq.rear = -1;

	while (done < num) {
		for (int i = 0; i < num; i++) {
			if (p[i].arrivalT == time) {
				insertQ(&rq, p, time, num);
				sort_priority(&rq);
			}
		}
		if (rq.front <= rq.rear) {
			printf("%d ", rq.p[rq.front].process_ID);
			rq.p[rq.front].CPU_burstT--;
			sort_priority(&rq);
		}
		else {
			printf(". ");
		}
		if (rq.p[rq.front].CPU_burstT == 0) {
			p[rq.p[rq.front].process_ID].turnaroundT = time - p[rq.p[rq.front].process_ID].arrivalT+1;
			p[rq.p[rq.front].process_ID].waittingT = p[rq.p[rq.front].process_ID].turnaroundT - p[rq.p[rq.front].process_ID].CPU_burstT; 
			done++;
			rq.front++;
		}
		time++;
	}
	printChart();

	return 0;
}

int RR(process p[], int num) {
	printf("\n\nRR\n\n");
	int tq;
	int time = 0;
	int first;
	int done = 0;

	readyQ rq;
	for (int i = 0; i < Qsize; i++) {
		rq.p[i].process_ID = -1;
	}
	rq.front = 0;
	rq.rear = 0;

	printf("input time quantum: ");
	scanf("%d", &tq);
	printf("\n");

	first = first_arrival(p, num);
	rq.p[rq.front] = p[first];
	insertQ(&rq, p, time, num);

	while (done != num) {
		while (time < rq.p[rq.front].arrivalT) {
			time++;
			insertQ(&rq, p, time, num);
			printf(". ");
		}
		for (int i = 0; i < tq; i++) {
			time++;
			insertQ(&rq, p, time, num);
			rq.p[rq.front].CPU_burstT--;
			if (rq.p[rq.front].CPU_burstT >= 0)
				printf("%d ", rq.p[rq.front].process_ID);
			if (rq.p[rq.front].CPU_burstT == 0) {
				break;
			}
		}
		if (rq.p[rq.front].CPU_burstT != 0) {
			if (rq.rear + 1 < Qsize)
				rq.p[++rq.rear] = rq.p[rq.front];
			else if (rq.rear + 1 == Qsize) {
				rq.rear = 0;
				rq.p[rq.rear] = rq.p[rq.front];
			}
		}
		else {
			p[rq.p[rq.front].process_ID].turnaroundT = time - rq.p[rq.front].arrivalT;
			p[rq.p[rq.front].process_ID].waittingT = p[rq.p[rq.front].process_ID].turnaroundT - p[rq.p[rq.front].process_ID].CPU_burstT;
			done++;
		}
		if (rq.front != rq.rear) {
			if (rq.front + 1 < Qsize)
				rq.front++;
			else if (rq.front + 1 == Qsize)
				rq.front = 0;
		}
	}
	printChart();

	return 0;
}

void reset(process p[], int num) {
	for (int i = 0; i < num; i++) {
		p[i].turnaroundT = 0;
		p[i].waittingT = 0;
	}
}

int first_arrival(process p[], int num) {
	int first = 0;
	int min_arrival;
	int burst;

	min_arrival = p[0].arrivalT;
	burst = p[0].CPU_burstT;
	for (int i = 1; i < num; i++) {
		if (p[i].arrivalT < min_arrival) {
			first = i;
			min_arrival = p[i].arrivalT;
			burst = p[i].CPU_burstT;
		}
		else if (p[i].arrivalT == min_arrival) {
			if (p[i].CPU_burstT < burst) {
				first = i;
				min_arrival = p[i].arrivalT;
				burst = p[i].CPU_burstT;
			}
		}
	}
	return first;
}

void insertQ(readyQ *rq, process p[], int time, int num) {
	int check = 0;
	for (int i = 0; i < num; i++) {
		for (int j = 0; j < num; j++) {
			if (p[i].process_ID == (*rq).p[j].process_ID) {
				check = 1;
			}
		}
		if ((p[i].arrivalT == time) && (check == 0)) {
			(*rq).rear++;
			(*rq).p[(*rq).rear] = p[i];
		}
		check = 0;
	}
}

void sort_arrival(readyQ * rq) {
   process temp;
   for (int i = (*rq).front; i < (*rq).rear; i++) {
      for (int j = i + 1; j <= (*rq).rear; j++) {
         if ((*rq).p[j].arrivalT < (*rq).p[i].arrivalT) {
            temp = (*rq).p[j];
            (*rq).p[j] = (*rq).p[i];
            (*rq).p[i] = temp;
         }
      }
   }
}

void sort_burst(readyQ * rq) {
	process temp;
	if ((*rq).front < (*rq).rear) {
		for (int i = (*rq).front; i < (*rq).rear; i++) {
			for (int j = i + 1; j <= (*rq).rear; j++) {
				if ((*rq).p[j].CPU_burstT < (*rq).p[i].CPU_burstT) {
					temp = (*rq).p[j];
					(*rq).p[j] = (*rq).p[i];
					(*rq).p[i] = temp;
				}
			}
		}
	}
}

void sort_priority(readyQ * rq) {
	process temp;
	for (int i = (*rq).front; i < (*rq).rear; i++) {
		for (int j = i + 1; j <= (*rq).rear; j++) {
			if ((*rq).p[j].priority < (*rq).p[i].priority) {
				temp = (*rq).p[j];
				(*rq).p[j] = (*rq).p[i];
				(*rq).p[i] = temp;
			}
		}
	}
}

void Evaluation(process p[], int num, float result[]) {
	float sum_waittingT = 0;
	float sum_turnaroundT = 0;
	float avg_waittingT = 0;
	float avg_turnaroundT = 0;

	for (int i = 0; i < num; i++) {
		sum_turnaroundT += p[i].turnaroundT;
		sum_waittingT += p[i].waittingT;
	}
	avg_waittingT = sum_waittingT / num;
	avg_turnaroundT = sum_turnaroundT / num;

	printf("\naverage turn around time: %4f\n", avg_turnaroundT);
	printf("average waitting time: %4f\n", avg_waittingT);

	for (int i = 0; i < 12; i++) {
		if (result[i] == 0) {
			result[i] = avg_turnaroundT;
			result[i + 1] = avg_waittingT;
			break;
		}
	}
}

void print_table(process p[], int num) {
	printf("\n\n  ID  TAT   WT\n");
	for (int i = 0; i < num; i++) {
		printf("%4d %4d %4d\n", p[i].process_ID, p[i].turnaroundT, p[i].waittingT);
	}
}

void printChart() {
	printf("\n");
	for (int i = 0; i < 50; i++) {
		printf("%d ", i%10);
	}
	printf("\n");
	for (int i = 0; i < 5; i++) {
		printf("%d                   ", i);
	}
}