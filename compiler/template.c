#include <stdio.h>
#include <setjmp.h>

int array[(int)1e6];

union jmp_buffer_union
{
	jmp_buf env_in_buf;
	struct {
		int env[64];	
	}env_in_int;
}env;

int val, i;

#define forward_jmp(position)								
	val = 0;												
	val=setjmp(env.env_in_buf); 							
	if(!val)			 									
		for(i = 0;i < 64;i++)								
			array[position + i] = env.env_in_int.env[i]

#define back_jmp(position) 									
	for(i = 0;i < 64;i++)									
		env.env_in_int.env[i] = array[position + i];		
	longjmp(env.env_in_buf, 1)


