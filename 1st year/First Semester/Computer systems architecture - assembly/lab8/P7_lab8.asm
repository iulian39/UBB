;7. Write a program which reads the name of a file from the keyboard and then it prints on the screen the odd lines from this file.
assume cs:code, ds:data

data segment
	msg db 'Name of the file: $'
	maxFileName db 12
	lFileName db ?
	fileName db 12 dup (?)
	buffer db 100 dup (?), '$'
	newBuffer db 100 dup (?), '$'
	contor dw 0
	divizor db 2
	save dw ?
	contorNBuffer dw 0
	openErrorMsg db 'File does not exist.$'
	readErrorMsg db "Can't read the file.$"
	newLine db 0ah, '$' ; \n character
data ends

code segment
start:
	mov ax, data
	mov ds, ax

	; print the string 'msg' to the screen
	mov ah, 09h
	mov dx, offset msg
	int 21h

	;read from the keyboard the name of the file
	mov ah, 0ah
	mov dx, offset maxFileName
	int 21h


	mov al, lFileName
	xor ah, ah
	mov si, ax
	mov fileName[si], 0

	;open the file
	mov ah, 3dh
	mov al, 0
	mov dx, offset fileName
	int 21h

	jc openError 
	mov bx, ax

	goOn:
		mov ah, 3fh
		mov dx, offset buffer
		mov cx, 100
		int 21h
		jc readError

		mov si, ax
		mov buffer[si], '$'

		mov si, 0
		mov di, 0
		; now iterate through the buffer and change the letters where needed
		next:
			cmp buffer[si], '$'
			je MaybeLastCompare
			cmp buffer[si], 0ah ; is it a new line ?
			jne _nu ; we are making the statistics
			je _da
			_da:		
				;sub contor, 1 ; we must decrement the contor in order to everything right. if there are 3characters and a \n the contor is 4(even)
				mov ax, contor ; ax = contor
				div divizor ; we check if the number is even or odd
				cmp ah, 0 ; ah = 0 -> even
				je movInNewBuffer
				mov contor, 0; we make the contor 0 and then we call next if the number is odd
				jmp next
			_nu:
				add contor, 1
				inc si
				jmp next ; inc si&contor and then we check the next character from the buffer
				
			movInNewBuffer:
				mov dx, si ; we save si in dx
				sub si, contor
				sub si, 1
				Again:
					inc si
					mov al, buffer[si]
					mov newBuffer[di], al ; we move the value from buffer to the new buffer and then we compare si with dx(its previous value)
					inc di
					cmp si, dx
					je IncSiAndNEXT ; we must incremet one more time si and then we move on and make contor 0
					jne Again 
				IncSiAndNEXT:
					mov contor, 0
					inc si
					jmp next
				

		MaybeLastCompare:
			cmp si, 100
			jne print
			je PrintAndGoOn
		print:
		mov newBuffer[di], '$'
		mov dx, offset newBuffer
		mov ah, 09h
		int 21h
		
		jmp endPrg
		PrintAndGoOn:
		mov newBuffer[di], '$'
		mov dx, offset newBuffer
		mov ah, 09h
		int 21h
		
		jmp goOn
	
	jmp endPrg

	openError:
		mov ah, 09h
		mov dx, offset openErrorMsg
		int 21h
		jmp endPrg
	
	readError:
		mov ah, 09h
		mov dx, offset readErrorMsg
		int 21h
	
	endPrg:
		mov ax, 4c00h
		int 21h
code ends
end start