assume cs:code, ds:data
data segment public
	tmp db 5 dup (?), 13, 10, '$'
data ends

code segment public
public tipar	; functia 'tipar' este vizibila si din alte module
tipar:
; intrare: ax = numarul de tiparit
; tipareste numarul din ax
; nu modifica restul registrilor; poate modifica ax

; salvam registrii ca sa-i putem folosi in procedura
	push bx
	push cx
	push dx
; calculam reprezentarea in baza 10
	mov bx, offset tmp+5  ; bx=adresa ultimei cifre scrise deja
	mov cx, 10	; cx = 10 (constant)
bucla:
	mov dx, 0
	cbw
	div cx	; dl=cifra curenta, ax=restul numarului
	dec bx
	add dl, '0'
	mov byte ptr [bx], dl
	cmp ax, 0
	jne bucla
; tiparim
	mov dx, bx
	mov ah, 09h
	int 21h
; refacem contextul
	pop dx
	pop cx
	pop bx
	ret

code ends
end