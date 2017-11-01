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

int main(){
    int c, i;
    int lunguser,lungpass;
    struct sockaddr_in server;
    char username[256],password[256] , *passwordrecv;
    c=socket(AF_INET,SOCK_STREAM,0);
    char salt[3];

    if(c<0){
        printf("Eroare la crearea socketului client \n");
        return 1;
    }

    memset(&server,0,sizeof(server));
    server.sin_port=htons(1030);
    server.sin_family=AF_INET;
    server.sin_addr.s_addr=inet_addr("127.0.0.1");

    if(connect(c,(struct sockaddr *)&server, sizeof(server))<0){
        printf("Eroare la conectare la server\n");
        return 1;

    }
    printf("Username: ");
    fgets(username,256,stdin);
    lunguser=strlen(username)-1;//Nu mai trimite si /n pentru comparare
    lunguser=htons(lunguser);
    send(c,&lunguser,sizeof(lunguser),0);// send lungimea usernameului

    send(c,username,lunguser*sizeof(char),0);

    printf("Password: ");
    fgets(password,256,stdin);

    password[strlen(password) - 1] = '\0';

    recv(c,&lungpass,sizeof(lungpass),MSG_WAITALL);//primesc lungimea parolei
    lungpass = ntohs(lungpass);
    passwordrecv = calloc(lungpass,sizeof(char));
    recv(c,passwordrecv,lungpass*sizeof(char),MSG_WAITALL);//primesc parola


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