# Activity II: Security Policy <!-- omit in toc -->

By Saenyakorn Siangsanoh 6232035721

# Table of Content <!-- omit in toc -->

- [Part I](#part-i)
  - [1.1](#11)
    - [Answer](#answer)
  - [1.2](#12)
    - [Answer](#answer-1)
  - [1.3](#13)
    - [Answer](#answer-2)
  - [1.4](#14)
    - [Answer](#answer-3)
- [Part II](#part-ii)
  - [2.1](#21)
    - [Answer](#answer-4)
  - [2.2](#22)
    - [Answer](#answer-5)
  - [2.3](#23)
    - [Answer](#answer-6)
  - [2.4](#24)
    - [Answer](#answer-7)

# Part I

Assume that you are about to open a 24-hour coffee shop on the Chulalongkorn University campus called “Too Late To Sleep”. The coffee shop must provide services to all members of Chulalongkorn University (no entrance fee) and to outsiders (charge for entrance).

## 1.1

Identify users and roles of all persons involved in the coffee shop (i.e., different types of customers, non-customers, etc.).

### Answer

| User                  | Role          | Note                                                                     |
| --------------------- | ------------- | ------------------------------------------------------------------------ |
| Manager               | Manager,Staff | เจ้าของร้าน                                                              |
| Staff                 | Staff         | คนที่คอยดูแลร้าน และบริการลูกค้า และต้องได้รับการลงทะเบียนจากเจ้าของร้าน |
| Mechanic              | Mechanic      | เป็นช่างเฉพาะกิจ ที่ขะเจ้ามาซ่อมบำรุงร้านค้า เมื่อมีอุปกรณ์ชำรุด         |
| Chulalongkorn Officer | Customer      | เจ้าหน้าที่ พนักงาน และอาจารย์ ในมหาวิทยาลัย                             |
| Student               | Customer      | นิสิตจุฬาลงกรณ์มหาวิทยาลัย                                               |
| Member                | Member        | สมาชิกร้านค้า                                                            |
| Outsider              | Outsider      | บุคคลภายนอกจุฬาลงกรณ์มหาวิทยาลัย                                         |

## 1.2

You can physically design the shop any way you like. Identify the services (resources) you want to support your different customers and whether or not you would like to create different zones with different services (resources). Your shop must at least have:

- One entrance door
- One bathroom
- One coffee service area
- Places to sit

You may add anything else you’d like. Describe the services (resources) in your shop

### Answer

| Resource             | Description                                      |
| -------------------- | ------------------------------------------------ |
| Shop                 | ร้านค้า                                          |
| Backoffice           | หลังร้าน ซึ่งเป็นที่เก็บของ เก็บสินค้า และอื่น ๆ |
| Toilet               | บริการในการเข้าห้องน้ำ                           |
| Bathroom             | บริการในการเข้าห้องอาบน้ำ                        |
| Service Area         | บริการในพื้นที่ให้บริการ                         |
| Coffee Bar           | บริการกาแฟ                                       |
| Financial Statements | ดูแลบริการงบการเงิน                              |
| Tool Maintenance     | การดูแลอุปกรณ์ หรือซ่อมบำรุงของในร้านค้า         |

## 1.3

Identify resources that require access

### Answer

| Resource             | Control Access                                                               |
| -------------------- | ---------------------------------------------------------------------------- |
| Shop                 | ทุกคนสามารถเข้าร้านค้าได้ ยกเว้นบุคคลภายนอก ต้องจ่ายขั้นต่ำ 100 บาท          |
| Backoffice           | เฉพาะบุคลากรของร้านค้าเท่านั้น (รวมถึงผู้ดูแลอุปกรณ์ด้วย)                    |
| Toilet               | ทุกคนสามารถใช้บริการห้องน้ำได้                                               |
| Bathroom             | ทุกคนสามารถใช้บริการห้องอาบน้ำได้ ยกเว้นบุคคลภายนอก                          |
| Service Area         | ทุกคนสามารถใช้บริการร้านค้าได้ ยกเว้นบุคคลภายนอก                             |
| Coffee Bar           | เฉพาะพนักงานร้านและผู้จัดการร้านเท่านั้น ที่สามารถเข้าถึงพื้นที่ให้บริการได้ |
| Financial Statements | เฉพาะผู้จัดการร้านที่สามารถดูแลงบการเงินภายในร้านค้าได้                      |
| Tool Maintenance     | เฉพาะผู้ดูแลอุปกรณ์ที่สามารถเข้าถึงการซ่อมบำรุงอุปกรณ์ได้                    |

## 1.4

Apply your knowledge to design the authorization system (e.g. access control) for your customers.

### Answer

| ​ Access             | Manager | Staff | Mechanic | Chulalongkorn Officer | Student | Member |           Outsider           |
| -------------------- | :-----: | :---: | :------: | :-------------------: | :-----: | :----: | :--------------------------: |
| Shop                 |    ✓    |   ✓   |    ✓     |           ✓           |    ✓    |   ✓    | (ต้องซื้อของขั้นต่ำ 100 บาท) |
| Backoffice           |    ✓    |  ✓​   |    ✓     |                       |         |        |                              |
| Toilet               |    ✓    |   ✓   |    ✓     |           ✓           |    ✓    |   ✓    |              ✓               |
| Bathroom             |    ✓    |   ✓   |    ✓     |           ✓           |    ✓    |   ✓    |                              |
| Service Area         |    ✓    |   ✓   |    ✓     |           ✓           |    ✓    |   ✓    |                              |
| Coffee Bar           |    ✓    |   ✓   |          |                       |         |        |                              |
| Financial Statements |    ✓    |       |          |                       |         |        |                              |
| Tool Maintenance     |         |       |    ✓     |                       |         |        |                              |

# Part II

Assuming that you are now in charge of a new Registration Systems of Chulalongkorn University, please finish the following exercise.

## 2.1

Identify users and roles of persons related to the service

### Answer

| User                 | Role                 | Note                                         |
| -------------------- | -------------------- | -------------------------------------------- |
| Registration Officer | Registration Officer | เจ้าหน้าที่ฝ่ายทะเบียน จุฬาลงกรณ์มหาวิทยาลัย |
| Advisor              | Teacher, Advisor     | อาจารย์ที่ปรึกษา                             |
| Teacher              | Teacher              | อาจารย์ในจุฬาลงกรณ์มหาวิทยาลัย               |
| Student              | Student              | นิสิตจุฬาลงกรณ์มหาวิทยาลัย                   |

## 2.2

Identify resources (data and objects)

### Answer

| Resource                             | Description                                                 |
| ------------------------------------ | ----------------------------------------------------------- |
| Course                               | Course เรียนทั้งหมดของจุฬาลงกรณ์มหาวิทยาลัย                 |
| Student Account - Personal Data      | ข้อมูลส่วนตัวของนิสิต เช่น ชื่อ นามสกุล วันเกิด และอื่น ๆ   |
| Student Account - Course             | วิชาที่กำลังรอการอนุมัติการลงทะเบียนเรียน                   |
| Student Account - Grade              | เกรดในแต่ละวิชาทั้งหมดของนิสิต                              |
| Student Account - Degree Certificate | ใบปริญาของนิสิต                                             |
| Student Account - Advisor            | ข้อมูลของอาจารย์ที่ปรึกษา                                   |
| Teacher Account - Personal Data      | ข้อมูลส่วนตัวของอาจารย์ เช่น ชื่อ นามสกุล วันเกิด และอื่น ๆ |
| Teacher Account - Course             | ข้อมูลรายวิชาที่อาจารย์เป็นเจ้าของ                          |
| Teacher Account - Student            | รายชื่อนิสิตที่อยู่ในความดูแลของอาจารย์ที่ปรึกษาคนหนึ่ง     |
| Registration Officer Account         | Account ของพนักงานทะเบียนจุฬา ฯ​ ที่จะคอยดำเนินงานด้านหลัง  |

## 2.3

Identify functions (actions for resources)

### Answer

| Function                    | Resource                                             | Description                                                             |
| --------------------------- | ---------------------------------------------------- | ----------------------------------------------------------------------- |
| Course Enrollment           | Student Account - Course                             | นิสิตสามารถลงทะเบียนเรียนในวิชาที่เลือกได้                              |
| Course Drop                 | Student Account - Course                             | นิสิตสามารถลดรายวิชาที่ลงทะเบียนไปแล้วได้                               |
| Course Withdraw             | Student Account - Course                             | นิสิตสามารถถอนรายวิชาที่ลงทะเบียนไปแล้วได้                              |
| Degree Certificate Request  | Student Account - Degree Certificate                 | นิสิตสามารถขอใบปริญญาได้                                                |
| Viewing Grade               | Student Account - Grade                              | นิสิตสามารถดูเกรดของจัวเองได้                                           |
| Viewing Schedule            | Student Account - Course                             | นิสิตสามารถดูตารางเรียนของตัวเองในเทอมนั้น ๆ ได้                        |
| Course Grading              | Student Account - Grade, Teacher Account - Course    | อาจารย์สามารถให้เกรดในวิชาตัวเองกับนิสิตที่ลงทะเบียนเรียนวิชานั้นได้    |
| Course Registration         | Course, Teacher Account - Course                     | อาจารย์สามารถส่งคำขอเพิ่มรายวิชาให้กับสำนักทะเบียนได้                   |
| Course Acceptance           | Course, Teacher Account - Course                     | สำนักงานทะเบียนสามารถตอบรับคำขอเพิ่มรายวิชาของอาจารย์ได้                |
| Course Rejection            | Course, Teacher Account - Course                     | สำนักงานทะเบียนสามารถไม่ตอบรับคำขอเพิ่มรายวิชาของอาจารย์ได้             |
| Assign Advisor              | Student Account - Advisor, Teacher Account - Student | อาจารย์สามารถกำหนดให้นิสิตมีอาจารย์ที่ปรึกษาเป็นตัวเองได้               |
| Assigning Student to Course | Course, Student Account - Course                     | สำนักงานทะเบียนสามารถทำให้การลงทะเบียนเรียนของนิสิตสำเร็จได้ แบบแรนด้อม |

## 2.4

Apply your knowledge to design the authorization system. Please specify whether the user (role) should be allowed to access the resource (read and write). Translate your design into an access control matrix.

### Answer

| Resources/Roles                      |       Teacher        |      Advisor       |                   Student                   |  Registration Officer   | Note                                                                            |
| ------------------------------------ | :------------------: | :----------------: | :-----------------------------------------: | :---------------------: | ------------------------------------------------------------------------------- |
| Course                               |  อ่าน (ทุก Course)   |         -          | อ่าน (เฉพาะ Course ที่ได้รับการอนุมัติแล้ว) | อ่าน/เขียน (ทุก Course) | Course ที่ได้รับการอนุมัติแล้ว คือ Course ที่อาจารย์ขอเพิ่มรายวิชา แล้วผ่านแล้ว |
| Student Account - Personal Data      |          -           |         -          |                 อ่าน/เขียน                  |            -            | นิสิตสามารถอ่านและแก้ไขข้อมูลส่วนตัวได้เสมอ                                     |
| Student Account - Course             |          -           |         -          |                    อ่าน                     |          เขียน          | Reg Officer จะเป็นคนกำหนดว่านิสิตลงทะเบียนสำเสร็จหรือไม่                        |
| Student Account - Grade              | แก้ไข (ให้เกรดนิสิต) | อ่าน (ออกใบปริญญา) |                    อ่าน                     |            -            | นิสิตอ่านได้อย่างเดียวให้เจ็บใจเล่น                                             |
| Student Account - Degree Certificate |          -           |         -          |                    อ่าน                     |          เขียน          | Reg Officer จะเป็นคนใส่ใบปริญญาให้นิสิตแต่ละคนในระบบ                            |
| Student Account - Advisor            |          -           |     อ่าน/เขียน     |                    อ่าน                     |            -            | ต้องเป็น Advisor ของนิสิตคนนั้นเท่านั้น ถึงจะอ่าน/เขียนได้                      |
| Teacher Account - Personal Data      |      อ่าน/เขียน      |         -          |                      -                      |            -            | อาจารย์สามารถอ่านและแก้ไขข้อมูลส่วนตัวได้เสมอ                                   |
| Teacher Account - Course             |      อ่าน/เขียน      |         -          |                    อ่าน                     |       อ่าน/เขียน        | Teacher สามารถแก้ไขข้อมูลได้ แต่ก็ยังต้องได้รับการอนุมัติจาก Reg ก่อนอยู่ดี     |
| Teacher Account - Student            |          -           |     อ่าน/เขียน     |                    อ่าน                     |            -            | นิสิตก็สามารถดูรายชื่อนิสิตที่ Advisor ของตัวเองดูแลได้                         |
| Registration Officer Account         |          -           |         -          |                      -                      |       อ่าน/เขียน        | แก้ password ของตัวเองได้ด้วย                                                   |
