import os

ann_dir = "/Users/rex/Desktop/anno/"
img_dir = "/Volumes/D221/WeaponS/"

os.chdir(img_dir)
#get dict of images
Ifiles = [ f for f in os.listdir('.') if os.path.isfile(f) and f[f.rfind('.')+1:] == "jpg"]
Ifiles = dict([i,1] for i in Ifiles) 


os.chdir(ann_dir)
#get list of xml annotations to be processed
Afiles = [ f for f in os.listdir('.') if os.path.isfile(f) and f[f.rfind('.')+1:] == "xml"]

#get list of already existing darknet annotations
Aefiles = [ f for f in os.listdir('.') if os.path.isfile(f) and f[f.rfind('.')+1:] == "txt"]
Aefiles = dict([i,1] for i in Aefiles) 

total = 0
for f in Afiles:
	if Ifiles.get( f[:f.rfind('.')]+".jpg" ) == None or Aefiles.get( f[:f.rfind('.')]+".txt" ) :
		continue
	
	print(ann_dir+f)
	f1 = open(ann_dir+f,"r+")
	f2 = open( ann_dir+f[:f.rfind('.') ]+".txt","w+")
	lines = f1.readlines()
	xmin = xmax = ymin = ymax = w = h = 0
	
	for l in lines:
		
		if l[ l.find('<') + 1 : l.find('>')] == "xmin" :
			xmin = float( l[ l.find('>') + 1 : l.rfind('<')] )
			
		elif l[ l.find('<') + 1 : l.find('>')] == "xmax" :
			xmax = float( l[ l.find('>') + 1 : l.rfind('<')] )
			
		elif l[ l.find('<') + 1 : l.find('>')] == "ymin" :
			ymin = float( l[ l.find('>') + 1 : l.rfind('<')] )
			
		elif l[ l.find('<') + 1 : l.find('>')] == "ymax" :
			ymax = float( l[ l.find('>') + 1 : l.rfind('<')] )
		
		elif l[ l.find('<') + 1 : l.find('>')] == "width" :
			w = float( l[ l.find('>') + 1 : l.rfind('<')] )
			
		elif l[ l.find('<') + 1 : l.find('>')] == "height" :
			h = float( l[ l.find('>') + 1 : l.rfind('<')] )
	
	xmin = format(xmin/w,'.6f')
	xmax = format(xmax/w,'.6f')
	ymin = format(ymin/h,'.6f')
	ymax = format(ymax/h,'.6f')
	f2.write("0"+" "+str(xmin)+" "+str(xmax)+" "+str(ymin)+" "+str(ymax))
	total = total+1
	f2.close()
	f1.close()
print(str(total) + " files processed.")	