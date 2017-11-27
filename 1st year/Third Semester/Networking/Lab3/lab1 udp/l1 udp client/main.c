#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>
#include <netinet/in.h>
#include <netinet/ip.h>
#include <string.h>
#include <arpa/inet.h>
#include <stdlib.h>
#include <unistd.h>
#include <netdb.h>

void error(char *msg)
{
    perror(msg);
    exit(0);
}

int main(){
    int i;
    int sock, length, n;
    struct hostent *hp;
    int lung1 = 0,lung2 = 0, list1[200], list2[200], lung3 = 0;
    struct sockaddr_in server, from;
    char username[256],password[256] , *passwordrecv;
    char salt[3];

    sock= socket(AF_INET, SOCK_DGRAM, 0);
    if (sock < 0) error("socket");

    server.sin_family = AF_INET;
    hp = gethostbyname("127.0.0.1");
    if (hp == 0) error("Unknown host");

    bcopy((char *)hp->h_addr, (char *)&server.sin_addr, hp->h_length);
    server.sin_port = htons(1030);
    length=sizeof(struct sockaddr_in);


    printf("The first list : ");

    do
    {
        scanf("%d", &i);
        list1[lung1++] = i;

    }while (i != 0);



    printf("The second list : ");

    do
    {
        scanf("%d", &i);
        list2[lung2++] = i;

    }while (i != 0);

    lung1--;
    int j = lung1;
    lung1=htons(lung1);

    n=sendto(sock,&lung1,sizeof(int),0,(struct sockaddr *)&server,length);
    if (n < 0) error("Sendto");


    for( i = 0; i < j; ++i)
    {
        list1[i] = htons(list1[i] );
        n=sendto(sock,&list1[i],sizeof(int),0,(struct sockaddr *)&server,length);
        if (n < 0) error("Sendto");
    }
    lung2--;
    j = lung2;
    printf("%d\n\n\n", lung2);
    lung2=htons(lung2);
    n=sendto(sock,&lung2,sizeof(int),0,(struct sockaddr *)&server,length);
    if (n < 0) error("Sendto");


    for( i = 0; i < j; ++i)
    {
        list2[i] = htons(list2[i] );
        n=sendto(sock,&list2[i],sizeof(int),0,(struct sockaddr *)&server,length);
        if (n < 0) error("Sendto");
    }

    printf("Output: \n");

    n = recvfrom(sock,&lung3,sizeof(int),0,(struct sockaddr *)&from, &length);
    if (n < 0) error("recvfrom");
    lung3 = ntohs(lung3);
    int x;



    for(i = 0; i < lung3; ++i)
    {
        n = recvfrom(sock,&x,sizeof(int),0,(struct sockaddr *)&from, &length);
        if (n < 0) error("recvfrom");
        x = ntohs(x);
        printf("%d\n", x);
    }



}