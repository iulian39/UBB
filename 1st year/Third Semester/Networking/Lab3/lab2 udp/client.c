#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>
#include <netinet/in.h>
#include <netinet/ip.h>
#include <string.h>
#include <arpa/inet.h>
#include <stdlib.h>


#define _XOPEN_SOURCE
#include <unistd.h>
#include <crypt.h>
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
    int lunguser,lungpass;
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


    printf("Username: ");
    fgets(username,256,stdin);
    lunguser=strlen(username)-1;//Nu mai trimite si /n pentru comparare
    lunguser=htons(lunguser);
    n=sendto(sock,&lunguser,sizeof(int),0,(struct sockaddr *)&server,length);
    if (n < 0) error("Sendto");

    n=sendto(sock,username,lunguser,0,(struct sockaddr *)&server,length);
    if (n < 0) error("Sendto");


    printf("Password: ");
    fgets(password,256,stdin);

    password[strlen(password) - 1] = '\0';

    n = recvfrom(sock,&lungpass,sizeof(int),0,(struct sockaddr *)&from, &length);
    if (n < 0) error("recvfrom");
    lungpass = ntohs(lungpass);
    passwordrecv = calloc(lungpass,sizeof(char));
    n = recvfrom(sock,passwordrecv,lungpass*sizeof(char),0,(struct sockaddr *)&from, &length);
    if (n < 0) error("recvfrom");


    if (strlen(passwordrecv) > 0) // exista userul
    {
        printf("Parola criptata e: %s\n",passwordrecv);

        strncpy(salt, passwordrecv, 2);
        salt[3] = '\0';

        char * buf = malloc(200 * sizeof(char));

        buf = crypt(password, salt);
        if (strcmp(buf, passwordrecv) == 0)
        {
            printf("Logare cu succes ! Salt = %s\n", salt);
        }
        else
        {
            printf("Parola incorecta :( \n" );
        }
    }
    else
    {
        printf("Username-ul nu exista\n");
    }



}