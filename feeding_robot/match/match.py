
import os 
import PIL.Image as Image 

########################

receive_fig='/home/longu/Desktop/match/sample2.jpg'
pic_folder='/home/longu/Desktop/match/database/'

########################
def difference(hist1,hist2): 
	sum1 = 0
	for i in range(len(hist1)):
		if (hist1[i] == hist2[i]): 
			sum1 += 1 
		else: 
			sum1 += 1 - float(abs(hist1[i] - hist2[i]))/ max(hist1[i], hist2[i]) 
	return sum1/len(hist1) 

def similary_calculate(path1 , path2 , mode): 
	if(mode == True): 
		img1 = Image.open(path1).resize((256,256)).convert('1') 
		img2 = Image.open(path2).resize((256,256)).convert('1')
		hist1 = list(img1.getdata()) 
		hist2 = list(img2.getdata())
		#print("\n------------------------") 
		return difference(hist1, hist2)

		# 预处理 
		img1 = Image.open(path1).resize((256,256)).convert('RGB') 
		img2 = Image.open(path2).resize((256,256)).convert('RGB') 
		if(mode == 1): 
			return difference(img1.histogram(), img2.histogram())
		if(mode == 2): 
			sum = 0; 
			for i in range(4): 
				for j in range(4): 
					hist1 = img1.crop((i*64, j*64, i*64+63, j*64+63)).copy().histogram() 
					hist2 = img2.crop((i*64, j*64, i*64+63, j*64+63)).copy().histogram() 
					sum += difference(hist1, hist2) 
					#print difference(hist1, hist2) 
			return sum/16 
		return 0 

def readfolder(dic,pic, mode):
# 不同的mode对应不同的类型
	file_list=os.listdir(dic) 
	t = 0 
	file_temp = ''

	for dic_name in file_list:
		folder=dic+'/'+dic_name
		for root,directors,files in os.walk(folder): 
			for filename in files: 
				filepath = os.path.join(root,filename)
				if (filepath.endswith(".png") or filepath.endswith(".jpg")): 	
					#remember = similary_calculate(pic,filename,mode) 			
					remember = similary_calculate(pic,filepath,mode)
					#print (filename) 
					#print (remember)
					if (remember > t) and remember!= 1: 
						file_temp = filename.split('_')[0] 
						t = remember 
	#print('*************************\n')					
	return file_temp 

if __name__ == '__main__': 

	print ("The most similary figure is :" + readfolder(pic_folder,receive_fig,True))
