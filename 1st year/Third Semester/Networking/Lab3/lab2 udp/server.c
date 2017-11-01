#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>
#include <netinet/in.h>
#include <netinet/ip.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <pwd.h>
#include <stdlib.h>

#define _XOPEN_SOURCE
#include <unistd.h>
#include <crypt.h>

void error(char *msg)
{
    perror(msg);
    exit(0);
}

int main(){

    int sock, length, fromlen, n;
    struct sockaddr_in server, from;
    int c,l;

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

    while(1){
        char *username;
        struct passwd *p;
        int lungime, ok = 0;
        int lungpass;

        n = recvfrom(sock,&lungime,sizeof(int),0,(struct sockaddr *)&from,&fromlen);
        if (n < 0) error("recvfrom");
        printf("S-a conectat un client.\n");

        lungime = ntohs(lungime);
        username = malloc(lungime*sizeof(char));

        n = recvfrom(sock,username,lungime*sizeof(char),0,(struct sockaddr *)&from,&fromlen);
        if (n < 0) error("recvfrom");

        while((p = getpwent()) != NULL)
        {
            if(strcmp(p->pw_name,username) == 0)
            {
                ok = 1;
                break;
            }
        }

        if (ok == 0)
        {
            int d = 1;
            char e = '\0';
            d = htons(d);
            n=sendto(sock,&d,sizeof(int), 0,(struct sockaddr *)&from,fromlen);
            if (n < 0) error("Sendto");

            n=sendto(sock,&e,sizeof(char), 0,(struct sockaddr *)&from,fromlen);
            if (n < 0) error("Sendto");
        }
        else
        {
            char * buf = malloc(200 * sizeof(char));

            buf = crypt(p->pw_passwd, "ab"); // criptez parola

            lungpass = strlen(buf);
            lungpass = htons(lungpass);

            n=sendto(sock,&lungpass,sizeof(int), 0,(struct sockaddr *)&from,fromlen);
            if (n < 0) error("Sendto");

            n=sendto(sock,buf,strlen(buf) * sizeof(char), 0,(struct sockaddr *)&from,fromlen);
            if (n < 0) error("Sendto");
            endpwent();

        }

        endpwent();
        close(c);


    }


}