#include<iostream>
#include<stdio.h>
using namespace std;

/*
Author: Landon Meuth
Creation Date:  20220101
Purpose:
maze
*/

int input() {
	
	input= getchar();

	/*HANDLE hstdin;
	DWORD  mode;
	int input=0;
	
	hstdin = GetStdHandle( STD_INPUT_HANDLE );
	GetConsoleMode( hstdin, &mode );
	SetConsoleMode( hstdin, ENABLE_ECHO_INPUT | ENABLE_PROCESSED_INPUT );  // see note below 
	
	int ch = cin.get();
	input=ch;
	
	SetConsoleMode( hstdin, mode );
	return input;*/
}

int main() {
	
	int xres = 10; //break number and horizontal length
	int yres = 10; //vertical length
	
	int preplotx;
	int preploty;
	int plotx=1;
	int ploty=1;
	
	long resolution = xres*yres;
	
	while(0==0) {
			
		//place your desired background graphics
		int display[resolution]= {
		1,1,1,1,1,1,1,1,1,1,
		1,0,0,0,1,0,1,1,3,1,
		1,1,1,0,1,1,1,1,0,1,
		1,0,1,0,0,1,1,1,0,1,
		1,0,1,1,0,1,0,0,0,1,
		1,0,1,0,0,1,0,1,1,1,
		1,0,1,0,1,1,0,0,0,1,
		1,0,1,0,1,1,1,1,0,1,
		1,0,0,0,0,0,0,0,0,1,
		1,1,1,1,1,1,1,1,1,1,
		};
		
		//beggining of input routine
		
		preplotx=plotx;
		preploty=ploty;
		
		int movput=input();
		
		if (movput==115) {
			preploty++;
		}
		
		if (movput==119) {
			preploty--;
		}
		
		if (movput==100) {
			preplotx++;
		}
		
		if (movput==97) {
			preplotx--;
		}
		
		if (display[preploty*xres+preplotx]==0) {
			plotx=preplotx;
			ploty=preploty;
		}
		
		if (display[preploty*xres+preplotx]==3) {
			cout << "YOU WIN!!!!";
			break;
		}
		
		system("cls");
		
		//place overhead graphics
		
		display[ploty*xres+plotx]=2;
		
		//beggining of drawing routine
		
		int i=0;
		int brk=0;

		for (int i = 0; i<resolution; i++) {
			if(brk==xres) {
				cout << "\n";
				brk=0;
			}
			if(display[i]==1) {
				cout << "#";
			}
			else if (display[i]==2){
				cout << "O";
			}
			else if (display[i]==3){
				cout << "W";
			}
			else {
				cout << ".";
			}
			brk++;
		}
		cout << "\n\n";
		
		//end of drawing routine
	}
	system("pause");
	return 0;
}

