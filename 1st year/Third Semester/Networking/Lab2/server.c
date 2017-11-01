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


int main(){

    int s;
    struct sockaddr_in server, client;
    int c,l;

    s=socket(AF_INET, SOCK_STREAM, 0);
    if(s<0){
        printf("Eroare la crearea socketului server \n");
        return 1;
    }

    memset(&server,0,sizeof(server));
    server.sin_port=htons(1030);
    server.sin_family=AF_INET;
    server.sin_addr.s_addr=INADDR_ANY;

    if(bind(s,(struct sockaddr*)&server,sizeof(server))<0){
        printf("Eroare la bind\n");
        return 1;
    }

    listen(s,5);

    l = sizeof(client);

    memset(&client,0,sizeof(client));
    while(1){
        char *username;
        struct passwd *p;
        int lungime, ok = 0;
        int lungpass;

        c=accept(s,(struct sockaddr*)&client,&l);
        printf("S-a conectat un client.\n");
        recv(c,&lungime,sizeof(lungime),MSG_WAITALL); // am primit lungimea
        lungime = ntohs(lungime);
        username = malloc(lungime*sizeof(char));

        recv(c,username,lungime*sizeof(char),MSG_WAITALL); // am primit usernameu
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

            send(c, &d, sizeof(int), 0); // trimit lungimea parolei
            send(c, &e, sizeof(char), 0);
        }
        else
        {
            char * buf = malloc(200 * sizeof(char));

            buf = crypt(p->pw_passwd, "ab"); // criptez parola

            //lungpass=strlen(p->pw_passwd);
            lungpass = strlen(buf);
            lungpass = htons(lungpass);

            send(c, &lungpass, sizeof(lungpass), 0); // trimit lungimea parolei
            send(c, buf, strlen(buf) * sizeof(char), 0);//trimit parola
            endpwent();

        }

        endpwent();
        close(c);


    }


}