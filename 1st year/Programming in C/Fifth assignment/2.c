//2. Replace all vowels with # in the text read from a given file.
#include <stdio.h>
#include <string.h>

int main()
{
    FILE *fpr = fopen("data.txt", "r");
    FILE *fpw = fopen("data2.txt","w");
    char c;
    while ((c = getc(fpr)) != EOF)
         { if (strchr("aeiouAEIOU",c))
              putc('#', fpw);
           else
              putc(c,fpw); }
    fclose(fpr);
    fclose(fpw);

    return 0;

}
