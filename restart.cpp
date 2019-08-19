#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

string command(string t, bool has_output = true)
{
	cout<<endl<<endl;
	cout<<"I'm about to do this command:"<<endl;
	cout<<t<<endl;
	
	string r = "";
	FILE *fp;
	char path[1035];
	
	/* Open the command for reading. */
	fp = popen(t.c_str(), "r");
	if (fp == NULL) {
		printf("Failed to run command\n" );
		return NULL;
	}
	
	if (has_output)
	{
		/* Read the output a line at a time - output it. */
		while (fgets(path, sizeof(path)-1, fp) != NULL) {
			r += path;
		}
	}
	
	/* close */
	pclose(fp);
	
	return r;
}

int main( int argc, char *argv[] )
{
	string output;
	
	command("cd /home/ec2-user/pnb");
	command("git pull origin master");
	output = command("ps -ax | grep python3");
	cout<<output<<endl;
	
	stringstream test(output.c_str());
	string segment;
	
	while(getline(test, segment, '\n'))
	{
		for (int i=0; i<segment.length(); i++)
		{
			if (segment.length() >0)
			{	
				if (segment[0] >= '0' && segment[0] <='9')
				{
					;
				}
				else
				{
					segment.erase(0,1);
				}
			}
		}
		
		int pos = -1;
		for (int i=0; i<segment.length(); i++)	
		{
			if (segment[i] == ' ')
			{
				pos = i;
				break;
			}
		}
		
		if (pos>0)
		{
			segment = segment.substr(0,pos);
			command("kill " + segment);
		}		
	}
	
	command("python3 main.py &", false);

	return 0;
}
