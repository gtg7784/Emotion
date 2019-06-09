// 지렁이 게임 - Emotion 프로젝트
// camalCase 로 작성
// 고태건, 박민준, 이다은, 김재현
#pragma warning(disable : 4996)

#include<stdio.h>
#include<windows.h>
#include<stdlib.h>
#include<time.h>
#include<conio.h>

int randX = 0; // 먹이 생성을 위한 랜덤 x 좌표
int randY = 0; // 먹이 생성을 위한 랜덤 y 좌표
int speed = 150; // 게임 속도

unsigned char warm[1403];
// 지렁이 머리가 몸통에 박았을 때 체크하는 거
// lim(y)*(lim(x)+1)+lim(x) => (y+1)(x*2+2)+(x*2+1)
// 왜냐하면 x는 2byte 니까

unsigned int removeTailCheck[51 * 26];
// pointHead와 pointTail을 포인터로 쓰임
// 지렁이의 꼬리가 지나가는 부분을 체크하기 위한 배열
// 배열의 값에는 맵의 좌표가 저장됨
// lim(x)*lim(y) => (x*2+1)(y+1)
// 왜냐하면 x는 2byte 니까

int pointHead;
// removeTailCheck의 포인터로 쓰임
// 지렁이의 몸이 커질때마다 포인터를 1씩 증가시키면서 포인터가 가리키는 값에는 커진 지렁이 몸의 위치값을 나타냄

int pointTail;
// removeTailCheck의 포인터로 쓰임
// 지렁이가 지나간 부분을 체크하여 없애주기 위한 포인터
// 지렁이가 움직일때마다 pointTail이 가리키는 부분에 저장된 맵의 좌표로 가서 지렁이가 지나간 부분을 없앰

// (x, y)로 커서를 이동시키는 함수
void setLocation(int x, int y) {
	COORD pos = { x - 1, y - 1 };
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), pos);
}

// 25 * 25 윤곽선 출력
void printBorder() {
	int x = 22;
	int y = 22;

	printf("%c%c", 0xa6, 0xa3); // ┌
	for (int i = 0; i < x; i++) {
		printf("%c%c", 0xa6, 0xa1); // ─
	}
	printf("%c%c\n", 0xa6, 0xa4); // ┐

	for (int i = 0; i < y; i++) {
		printf("%c%c", 0xa6, 0xa2); // │
		for (int j = 0; j < x; j++) {
			printf("  ");
		}
		printf("%c%c\n", 0xa6, 0xa2); // │
	}

	printf("%c%c", 0xa6, 0xa6); // └
	for (int i = 0; i < x; i++) {
		printf("%c%c", 0xa6, 0xa1); // ─
	}
	printf("%c%c\n", 0xa6, 0xa5); // ┘
}

int makeFeed() {
	randX = (rand() % 22) * 2 + 3; // 난수 생성하여 먹이의 x 좌표 설정
	randY = (rand() % 22) + 2; // 난수 생성하여 먹이의 y 좌표 설정
	setLocation(randX, randY); // 먹이 좌표로 이동
	printf("□"); // 먹이 출력
	return randX, randY;
}

void gameover() {
	system("cls"); // 화면을 지운다
	setLocation(10, 10); // (30, 10) 좌표로 커서 이동
	printf("GAME OVER\n");
}

int main() {
	unsigned char menu = 2; // 게임 스타트 체크
	int x = 3; // 지렁이의 x 좌료 값
	int y = 2; // 지렁이의 y 좌표 값
	int prevX; // 지렁이가 지나간 좌표의 x 값
	int prevY; // 지렁이가 지나간 좌표의 y 값
	int warmBody; // 지렁이의 몸통 개수
	unsigned char key; // 입력값
	srand(time(NULL)); // 난수 초기화

	while (1) {
		prevX = 3;
		prevY = 2;
		key = 99;
		pointHead = 1;
		pointTail = 0;
		warmBody = 1;
		memset(removeTailCheck, 0, 1725);
		removeTailCheck[0] = 155;


		printf("Emotion Warm Game ! \n");
		printf("press 1 to start game \n");
		printf("press 0 to quit gmae \n");
		menu = getch();
		if (menu == '0') {
			break;
		}
		else if (menu != '1') {
			continue;
		}

		setLocation(1, 1);
		printBorder();
		makeFeed();
		setLocation(x, y); // 지렁이 시작 좌표로 이동

		while (1) {
			if (kbhit() == 1) {
				key = getch(); // 키 입력

				// 확장키일 경우
				if (key == 0x00 || key == 0xe0) {
					key = getch();
				}
			}

			if (key == 72) { // ↑
				y -= 1;
				if (y < 2) {
					gameover();
					break;
				}
			}
			else if (key == 80) { // ↓
				y += 1;
				if (y > 23) {
					gameover();
					break;
				}
			}
			else if (key == 75) { // ←
				x -= 2;
				if (x < 3) {
					gameover();
					break;
				}
			}
			else if (key == 77) { // →
				x += 2;
				if (x > 45) {
					gameover();
					break;
				}
			}

			// 먹이를 먹었을 때
			if (x == randX && y == randY) {

				makeFeed();

				//아래 코드는 지렁이가 먹이를 먹었으므로 새로이 추가된 몸통 좌표를 추가하고 지렁이의 자취좌표를 추가하는 것
				removeTailCheck[pointHead] = (y) * 45 + x; // 지렁이의 자취를 맵좌표값으로 추가
				pointHead++;

				if (pointHead >= 1656) {
					pointHead = 0;
				}
				warm[(y) * 45 + x] = 1; //몸통 좌표 추가(1이 몸통이 있다는 표시, 0이 몸통이 없다는 표시)
				warmBody++;

				if (warmBody >= 10) {
					speed -= 10;
					if (speed < 40) {
						speed = 40;
					}
					warmBody = 0;
				}
				continue;
			}

			//꼬리가 지나간 부위를 지우기 위한 코드임
			prevY = removeTailCheck[pointTail] / 45;  // prevX에 임시저장
			prevX = removeTailCheck[pointTail] % 45;
			if (prevX == 0) {
				prevX = 75;
			}
			setLocation(prevX, prevY);
			printf("%c%c", 0x00, 0x00);
			warm[removeTailCheck[pointTail]] = 0; //지렁이가 지나간 좌표는 몸이 존재하지 않으므로 몸통좌표에서 삭제
			pointTail++;
			if (pointTail >= 1656) {
				pointTail = 0;
			}

			//지렁이 머리가 가는 방향으로 지렁이 머리를 새로이 그려넣기 위한 코드임
			removeTailCheck[pointHead] = (y) * 45 + x;
			if (warm[removeTailCheck[pointHead]] == 0) { //지렁이 머리가 있을 곳에 지렁이 몸통이 없을 경우
				warm[removeTailCheck[pointHead]] = 1;
			}
			else {
				gameover(); //지렁이 머리와 몸통좌표가 겹쳤을 경우로, gameover임
				break;
			}
			pointHead++;
			if (pointHead >= 1656) {
				pointHead = 0;
			}

			setLocation(x, y);
			printf("□"); //지렁이 머리를 그린다x

			Sleep(speed); // 게임의 스피드 조절
		}
	}
}

