#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>
#include <netinet/in.h>
#include <netinet/ip.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <stdlib.h>

int IsInList(uint16_t* List, uint16_t LenList, uint16_t element)
{
    uint16_t i;

    for ( i = 0; i < LenList; ++i)
    {
        if ( element == List[i])
            return 1;
    }

    return 0;
}

void error(char *msg)
{
    perror(msg);
    exit(0);
}

int main() {
    int sock, length, fromlen, n;
    struct sockaddr_in server, from;
    int c,l;
    uint16_t lenList1, lenList2, lenUncommonList, i, j;

    sock=socket(AF_INET, SOCK_DGRAM, 0);
    if (sock < 0) error("Opening socket");
    length = sizeof(server);
    bzero(&server,length);
    server.sin_family=AF_INET;
    server.sin_addr.s_addr=INADDR_ANY;
    server.sin_port=htons(1030);

    if (bind(sock,(struct sockaddr *)&server,length)<0)
        error("binding");

    fromlen = sizeof(struct sockaddr_in);

    while (1) {
        lenUncommonList = 0;


        n = recvfrom(sock,&lenList1,sizeof(lenList1),0,(struct sockaddr *)&from,&fromlen);
        if (n < 0) error("recvfrom");
        //first array
        lenList1 = ntohs(lenList1);

        printf("S-a conectat un client.\n");

        uint16_t * list1 = malloc(lenList1 * sizeof(uint16_t));
        for ( i = 0; i < lenList1; i++)
        {
            n = recvfrom(sock,&list1[i],sizeof(list1[i]),0,(struct sockaddr *)&from,&fromlen);
            if (n < 0) error("recvfrom");
            list1[i] = ntohs(list1[i]);
        }

        //second array
        n = recvfrom(sock,&lenList2,sizeof(lenList2),0,(struct sockaddr *)&from,&fromlen);
        if (n < 0) error("recvfrom");
        lenList2 = ntohs(lenList2);

        uint16_t * list2 = malloc(lenList2 * sizeof(uint16_t));
        for ( i = 0; i < lenList2; i++)
        {
            n = recvfrom(sock,&list2[i],sizeof(list2[i]),0,(struct sockaddr *)&from,&fromlen);
            if (n < 0) error("recvfrom");
            list2[i] = ntohs(list2[i]);
        }

        //we build the 3rd array
        uint16_t * uncommonList = malloc(lenList1 * sizeof(uint16_t));
        for(i = 0; i < lenList1; i++)
        {
            if (!IsInList(list2, lenList2, list1[i]))
                uncommonList[lenUncommonList++] = list1[i];
        }

        j = lenUncommonList; // we use j because we dont need it anymore for the for loop and lenUncommonList might change after htons
        lenUncommonList = htons(lenUncommonList);
        n=sendto(sock,&lenUncommonList,sizeof(lenUncommonList), 0,(struct sockaddr *)&from,fromlen);
        if (n < 0) error("Sendto");

        for(i = 0; i < j; ++i)
        {
            uncommonList[i] = htons(uncommonList[i]);
            n=sendto(sock,&uncommonList[i],sizeof(uncommonList[i]), 0,(struct sockaddr *)&from,fromlen);
            if (n < 0) error("Sendto");
        }

        close(c);
        if ( NULL != list1)
        {
            free(list1);
            list1 = NULL;
        }

        if ( NULL != list2)
        {
            free(list2);
            list2 = NULL;
        }

        if ( NULL != uncommonList)
        {
            free(uncommonList);
            uncommonList = NULL;
        }

        // sfarsitul deservirii clientului;
    }
}