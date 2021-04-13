# importing libraries 
import cv2 

# Create a VideoCapture object and read from input file 
cap = cv2.VideoCapture('Nighttime.mp4') 

# Check if video captured successfully 
if (cap.isOpened()== False): 
    print("Error opening video file") 

# Read until video is completed 
while(cap.isOpened()): 
	
# Capture frame-by-frame 
    ret, frame = cap.read()
#turning the video frames to grayscale from RGB
    grayframe=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#turning the grayscale video frames to binary
    mask=cv2.threshold(grayframe, 240, 255, cv2.THRESH_BINARY)[1]
#Removing some noises in the frames
    mask=cv2.erode(mask,None,iterations=2)
    mask=cv2.dilate(mask,None,iterations=3)
    contours0, hierarchy=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours0:
        area = cv2.contourArea(cnt)
        print(area)
      
            #Tracking
        m = cv2.moments(cnt)
        cx = int(m['m10']/m['m00'])
        cy = int(m['m01']/m['m00'])
        x,y,w,h = cv2.boundingRect(cnt)
            
        cv2.circle(frame,(cx,cy),5,(0,0,255),-1)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        
    
        
        
    
    if ret == True: 

	# Display the resulting frame 
    	cv2.imshow('Frame', frame)

	# Press Q on keyboard to exit 
    	if cv2.waitKey(25) & 0xFF == ord('q'): 
            break

# Break the loop 
    else:
            break

# When everything done, release 
# the video capture object 
cap.release() 

# Closes all the frames 
cv2.destroyAllWindows() 
