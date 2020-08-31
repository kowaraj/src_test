//  scope.c

#include <stdio.h>
#include <string.h>
#include <stdint.h>
#include <stdlib.h>
#include <ctype.h>
#include <signal.h>
#include <time.h>
#include <pthread.h>
#include <errno.h>
#include <termios.h>
#include <fcntl.h>
#include <sys/ioctl.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <sys/time.h>
#include <sys/timeb.h>
#include <sys/types.h>
//#include <libusb-1.0/libusb.h>
#include <unistd.h>
#include <math.h>


#define TRUE   1
#define FALSE  0
typedef unsigned char gbool;
//~----------------------------------------------------------------------------
int main(int argc, char *argv[]) {

  int fin,status,numberbytes;
  char fname[80]="m6_1.bin";
  unsigned short buf[0x14000];
  int i,j,k,nturn,nt=0,nsectors=0;
  double sum[18]={18*0},sector[18],Srpm;
  double x,sum2[18]={18*0},sigma[18],sumall=0,sectorM;
  
  //	printf("speed=");
  //	scanf("%d",&Srpm);
  //        Srpm = 6000;
  //	printf("%d\n",Srpm);
  //	sector0=1000000./12./(Srpm/60.);

       	printf("file=");
       	scanf("%s",fname);

	printf("open %s\n",fname);

	fin = open(fname,O_RDONLY);
	if (fin == -1) {
	  printf("open file error %s  error=%d\n",fname,fin);
	  return(1);
	}

	numberbytes = read(fin, (char *)buf, sizeof(buf));
	if (numberbytes == -1) printf("errno=%d\n",errno);
	printf("read %d\n", numberbytes);
	close(fin);

	for (k=0; (0x8000 & buf[k]) == 0; k++) ;
	printf("%d  %04x\n",k,buf[k]);
	nturn = (numberbytes/2-k)/18-1;
	printf("nturn=%d\n",nturn);

	for (j=0; j<nturn; j++) {
	  
	  for (i=0; i<18; i++){
	    nsectors++;
	    if ((0x8000 & buf[18*j+i+k]) != 0) nt++;
	    x = ((0x7fff & buf[18*j+i+k])+.5)/5.;
	    sum[i] += x;
	    sum2[i] += x*x;
	    sumall += x;
	  //printf("%04x ", buf[18*j+i+k]);
	  }
	  //printf("\n");
	}
	sectorM = sumall/nsectors;
	Srpm = 60.*1000000./(18*sectorM);
 
printf("Nturns=%d RPM=%7.1f sec ava=%6.2f nsectors=%8d\n",nt,Srpm,sectorM,nsectors);

	for (i=0; i<18; i++) {
	  sector[i] = sum[i]/nt;
	  sigma[i] = sqrt((sum2[i] - sum[i]*sum[i]/nt)/nt); 
	  // sector[i] = sum[i]/nturn;
	  // sigma[i] = sqrt((sum2[i] - sum[i]*sum[i]/nturn)/nturn); 
	  printf("sec %2d  %7.2f usec  %7.2f  %5.1f   %5.2f",
		 i,sector[i],sectorM-sector[i],
		 100.*(sectorM-sector[i])/sectorM,sigma[i]);
	  printf("\n");
	}
	printf("\n");

	return(0);
}
