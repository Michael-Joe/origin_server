/*
 * File:   time_serv_multiprocess.c
 * Author: mjoe
 *
 * Create on 2017年12月02日，16:26
 */

#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <unistd.h>//read(),write()
#include <string.h>
#include <signal.h>
#include <sys/wait.h>
#include <stddef.h>//NULL的定义
#include <time.h>
#include <errno.h>

#define SERVERPORT 9271

void sig_chld( int signo );

int main(int argc,char** argv){
	int listenfd,connfd;
	int rtn;//存储bind()的返回值
	pid_t childpid;
	struct sockaddr_in cliaddr,servaddr;
	time_t timer;//用来获得当前时间

	listenfd = socket(AF_INET,SOCK_STREAM,0);//创建socket
	if (listenfd < 0 ){
		printf("socket error:%s\n",strerror(errno));
		exit(-1);
	}

	bzero(&servaddr,sizeof(servaddr));
	servaddr.sin_family      = AF_INET;
	servaddr.sin_addr.s_addr = htonl(INADDR_ANY);//inet_addr("0.0.0.0");
	servaddr.sin_port        = htons(SERVERPORT);//SERVERPORT("9271")

	rtn = bind(listenfd,(struct sockaddr *)&servaddr,sizeof(servaddr));//绑定IP和端口
	if (rtn != 0){
		close(listenfd);
		printf("bind error:%s\n",strerror(errno));
		exit(-1);
	}

	listen(listenfd,20);

	for(;;){
		int clilen = sizeof(cliaddr);
		connfd = accept(listenfd,(struct sockaddr *)&cliaddr,&clilen);

		if((childpid = fork()) == 0){
			close(listenfd);//关闭子进程里的监听

			struct tm *tblock;
			timer = time(NULL);
			tblock = localtime(&timer);//通过上三行获取本地时间
			//write(connfd,asctime(tblock),sizeof(struct tm));//将时间写回套接字
			write(connfd,"Hello World!",sizeof("Hello World!"));
			exit(0);
		}
		else
			signal(SIGCHLD,&sig_chld);
		close(connfd);//父进程关闭监听
	}

}

void sig_chld( int signo ) {
	pid_t pid;
	int stat;
	pid = wait(&stat);    
	printf( "child %d exit\n", pid );
	return;
}

