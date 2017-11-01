#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>
#include <netinet/in.h>
#include <netinet/ip.h>
#include <string.h>
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

int main() {
    int s;
    struct sockaddr_in server, client;
    int c, l;
    uint16_t lenList1, lenList2, lenUncommonList, i, j;

    s = socket(AF_INET, SOCK_STREAM, 0);
    if (s < 0) {
        printf("Eroare la crearea socketului server\n");
        return 1;
    }

    memset(&server, 0, sizeof(server));
    server.sin_port = htons(1234);
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = INADDR_ANY;

    if (bind(s, (struct sockaddr *) &server, sizeof(server)) < 0) {
        printf("Eroare la bind\n");
        return 1;
    }

    listen(s, 5);

    l = sizeof(client);
    memset(&client, 0, sizeof(client));

    while (1) {
        lenUncommonList = 0;

        c = accept(s, (struct sockaddr *) &client, &l);

        printf("S-a conectat un client.\n");

        //first array
        recv(c, &lenList1, sizeof(lenList1), MSG_WAITALL); // we get the len and then we get the array
        lenList1 = ntohs(lenList1);

        uint16_t * list1 = malloc(lenList1 * sizeof(uint16_t));
        for ( i = 0; i < lenList1; i++)
        {
            recv(c, &list1[i], sizeof(list1[i]), MSG_WAITALL);
            list1[i] = ntohs(list1[i]);
        }

        //second array
        recv(c, &lenList2, sizeof(lenList2), MSG_WAITALL);
        lenList2 = ntohs(lenList2);

        uint16_t * list2 = malloc(lenList2 * sizeof(uint16_t));
        for ( i = 0; i < lenList2; i++)
        {
            recv(c, &list2[i], sizeof(list2[i]), MSG_WAITALL);
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
        send(c, &lenUncommonList, sizeof(lenUncommonList), 0);

        for(i = 0; i < j; ++i)
        {
            uncommonList[i] = htons(uncommonList[i]);
            send(c, &uncommonList[i], sizeof(uncommonList[i]), 0);
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