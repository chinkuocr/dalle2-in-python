import os
import sys
import openai

openai.api_key="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"
#print("image_url = ",image_url)
#print("cmd = ",cmd)

#Sort the file names and find the max number
def find_max_file_number(folder):
	print("folder = ",folder)
	count = 0
	for path in os.scandir(folder):
	  if path.is_file():
	  	  count += 1
	return count


def create(argv):
	print(argv[0])
	cmd = 'mkdir "'+ argv[0] + '" '
	os.system(cmd)
	
	#file_num = find_max_file_number('"'+ argv[0] + '" ')
	file_num = find_max_file_number(argv[0])
	print("file_num = ", file_num)
	
	response = openai.Image.create(prompt=argv[0], n=10, size="1024x1024")
	for i in range(10):
		image_url = response['data'][i]['url']
		cmd = 'wget "' + image_url + '"  -O ' +  str(i + int(file_num)) + '.jpeg'
		os.system(cmd)
		
		cmd = 'move ' + str(i + int(file_num)) + '.jpeg "'+ argv[0] + '" '
		os.system(cmd)

def edit(argv):
	print("argv[1] = ", argv[1])
	print("argv[2] = ", argv[2])
	print("argv[3] = ", argv[3])
	
	cmd = 'mkdir "'+ argv[3] + '" '
	os.system(cmd)
	
	file_num = find_max_file_number(argv[3])
	print("file_num = ", file_num)
	
	response = openai.Image.create_edit( image=open(argv[1], "rb"), mask=open(argv[2], "rb"), prompt=argv[3],n=10, size="1024x1024")
	for i in range(10):
		image_url = response['data'][i]['url']
		cmd = 'wget "' + image_url + '"  -O ' +  str(i + int(file_num)) + '.jpeg'
		os.system(cmd)
		
		cmd = 'move ' + str(i + int(file_num)) + '.jpeg "'+ argv[3] + '" '
		os.system(cmd)

#response = openai.Image.create_edit( image=open("man.png", "rb"), mask=open("manmask.png", "rb"),  prompt="A cute baby sea otter wearing a beret",n=2, size="512x512")

if __name__ == "__main__":
   #sample command: python openai_test.py "Mona Lisa of AI Art Style"
   #create(sys.argv[1:])
   
   edit(sys.argv)














