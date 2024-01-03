import cv2
img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Sun",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)   

)



cv2.putText(img,
           "Mercury",
          (100,250),
         cv2.FONT_HERSHEY_COMPLEX,
           0.5,
         (255,255,255)   

)

cv2.putText(img,
            "Venus",
            (180,170),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)   

)

cv2.putText(img,
            "Earth",
            (270,270),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (355,355,355)   

)

cv2.putText(img,
            "Mars",
            (370,150),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (355,355,355)   

)

cv2.putText(img,
            "Jupiter",
            (480,400),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (355,355,355)   

)

cv2.putText(img,
            "Saturn",
            (750,350),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (355,355,355)   

)

cv2.putText(img,
            "Uranus",
            (970,320),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (355,355,355)   

)

cv2.putText(img,
            "Neptune",
            (1150,320),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (355,355,355)   

)

cv2.imshow("output",img)
cv2.waitKey(0)

#cv2.imwrite("solar_systemwithname.jpg",img)