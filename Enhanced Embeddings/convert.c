#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <pthread.h>
#include <time.h>

#define _FILE_OFFSET_BITS 64
#define MAX_STRING_LENGTH 1000

typedef double real;
typedef struct cooccur_rec {
    int word1;
    int word2;
    real val;
} CREC;

int main(){
    CREC cr;
    FILE *fin, *fout;
    fin  = fopen("cooccurrence.bin", "rb");
    fout = fopen("cooccurrence.txt", "w");
    int i = 0;
    while(1){
        fread(&cr, sizeof(CREC), 1, fin);
        if(feof(fin)) break;
        if (cr.word1 < 1 || cr.word2 < 1) { continue; }
        fprintf(fout, "%d\t%d\t%f\n", cr.word1, cr.word2, cr.val);
    }
    fclose(fin);
    fclose(fout);
}