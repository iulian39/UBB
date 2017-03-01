;7. Three character strings are given. Print on the screen the longest prefix for each of the three pairs of two strings that can be formed.
assume cs:code, ds:data

data segment public
	sir1 db 20, 30, 32, 15, 47, 21
	len1 equ $-sir1
	sir2 db 20, 30, 0, 15, 47, 21
	final_sir2 label word
	len2 equ $-sir2
	sir3 db 20, 30, 0, 15, 47, 21
	final_sir3 label word
	len3 equ $-sir3
	cnt1 dw 0
	cnt2 dw 0
	cnt3 dw ?
	sirnou1 db 50 dup(?)
	final_sir1 label word
	sirnou2 db 50 dup(?)
	sirnou3 db 50 dup(?)
data ends

code segment public
extrn	tipar:proc
start:
	mov ax, data
	mov ds, ax
	mov ax, len1
	cmp ax, len2
	jbe Len1a
	ja Len2a
	Len1a:
		mov cx, len1
		jmp startN
	Len2a:
		mov cx, len2
	
	startN:
	xor ax,ax
	xor bx,bx
	xor si,si
	xor di,di

	first:
		mov di, 0
		add di, cnt1 ;cnt1 is for sir2
		mov bl, sir2[di]
		add cnt1, 1
		cmp sir1[si], bl
		je putInSir1
		jne printOne
	putInSir1:
		mov al, sir1[si]
		mov di, 0
		add di, cnt2
		mov sirnou1[di], al
		inc si
		add cnt2, 1
		loop first
	
	printOne:
		mov cx, cnt2
		mov si, offset sirnou1
	_printOne:
		 ; we must find how many elements does sirnou have
		;cmp si, offset final_sir1
		;je continue
		lodsb
		call tipar
		;inc si
		;xor ax, ax
		loop _printOne
	
	continue:
		mov ax, len1
		cmp ax, len3
		jbe _Len1
		ja Len3a
	_Len1:
		mov cx, len1
		jmp _second
	Len3a:
		mov cx, len2
		
		
	_second:
		mov sirnou1[si], '$'
		mov si, 0
		mov di, 0
		mov cnt1, 0
		mov cnt2, 0
		second:
			mov di, 0
			add di, cnt1
			mov bl, sir3[di]
			add cnt1, 1
			cmp sir1[si], bl
			je putInSir2
			jne printTwo
	putInSir2:
		mov al, sir1[si]
		mov di, 0
		add di, cnt2
		mov sirnou2[di], al
		inc si
		add cnt2, 1
		loop second
		
	
	printTwo:
		mov cx, cnt2
		mov si, offset sirnou2
	_printTwo:
		lodsb
		call tipar
		;inc si
		;xor ax, ax
		loop _printTwo
		
	_continue:	
		mov ax, len2
		cmp ax, len3
		jbe _Len2
		ja _Len3
		_Len2:
			mov cx, len2
			jmp _third
		_Len3:
			mov cx, len3
		
	_third:
		mov sirnou2[si], '$'
		mov si, 0
		mov di, 0
		mov cnt1, 0
		mov cnt2, 0
		third:
			mov di, 0
			add di, cnt1
			mov bl, sir3[di]
			add cnt1, 1
			cmp sir2[si], bl
			je putInSir3
			jne printThree
	putInSir3:
		mov al, sir2[si]
		mov di, 0
		mov di, cnt2
		mov sirnou3[di], al
		inc si
		add cnt2, 1
		loop third
	
	printThree:
		mov cx, cnt2
		mov si, offset sirnou3
	_printThree:
		
		lodsb
		call tipar
		;inc si
		;xor ax, ax
		loop _printThree
		
		
	final:
	mov sirnou3[si], '$'
	mov ax, 4C00h
	int 21h
code ends
end start