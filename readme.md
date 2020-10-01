## LINE Message Object

- ตัวอย่าง Custom Payload ในรูปแบบต่าง ๆ สำหรับการแสดงผลบน LINE
- ตัวโครงสร้างออกแบบให้สามารถใช้งานร่วมกับ [Botnoi NLP Tool ใน Class เรียนสร้าง Chatbot](https://medium.com/botnoi-classroom/%E0%B8%84%E0%B8%A3%E0%B8%B1%E0%B9%89%E0%B8%87%E0%B9%81%E0%B8%A3%E0%B8%81%E0%B8%82%E0%B8%AD%E0%B8%87%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%80%E0%B8%9B%E0%B8%B4%E0%B8%94%E0%B9%80%E0%B8%9C%E0%B8%A2%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%AA%E0%B8%A3%E0%B9%89%E0%B8%B2%E0%B8%87-botnoi-%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%AB%E0%B8%A5%E0%B8%B1%E0%B8%81%E0%B8%AA%E0%B8%B9%E0%B8%95%E0%B8%A3%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%AA%E0%B8%A3%E0%B9%89%E0%B8%B2%E0%B8%87%E0%B9%81%E0%B8%8A%E0%B8%97%E0%B8%9A%E0%B8%AD%E0%B8%97-447dfc471d6e "Botnoi NLP Tool ใน Class เรียนสร้าง Chatbot")
- โครงสร้างของอ้างอิงจาก [LINE Developers Reference](https://developers.line.biz/en/reference/messaging-api/#message-objects "Line Developers Reference") และใช้ LINE Bot Designer ในการออกแบบ

## วิธีการใช้งานผ่าน APIs 
**สำหรับท่านที่ไม่ใช่ Developers** และต้องการใช้งานทันทีสามารถเรียกใช้ในลักษณะ APIs โดยแบ่งตาม Objects ได้ดังนี้ (ไม่ต้องส่งค่า parameter ใดเรียกใช้ได้เลย)
- ##### **Buttons template**
URL: https://line-message-object.herokuapp.com/buttons-template

	![](https://i.imgur.com/WiTBibE.jpg)
- ##### **Confirm-template**
URL: https://line-message-object.herokuapp.com/confirm-template

	![](https://i.imgur.com/GAL52hU.jpeg)
- ##### **Carousel-template**
URL: https://line-message-object.herokuapp.com/carousel-template

	![](https://i.imgur.com/ujEoywU.jpg)
- ##### **Image-carousel-template**
URL: https://line-message-object.herokuapp.com/image-carousel-template

	![](https://i.imgur.com/vkRIiDN.jpg)
- ##### **Flex-message**
URL: https://line-message-object.herokuapp.com/flex-message

	![](https://i.imgur.com/5UofsaI.jpeg)

## สำหรับสาย Developers
สามารถ Clone Project ไปลองใช้งานได้เลยครับ (ในรายละเอียดเพิ่มเติมจะอธิบายในภายหลัง)
