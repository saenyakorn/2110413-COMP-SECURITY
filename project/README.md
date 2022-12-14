# Term Project <!-- omit in toc -->

By Saenyakorn Siangsanoh 6232035721

The purpose of this project is to educate you with the fundamentals of security in web applications (secure coding) by fixing the vulnerable application.

# Table of Contents <!-- omit in toc -->

- [How to start DVWA](#how-to-start-dvwa)
- [Instructions](#instructions)
- [Vulnerabilities](#vulnerabilities)
  - [1. Bruce Force](#1-bruce-force)
    - [Exploitability](#exploitability)
    - [Weakness Prevalence](#weakness-prevalence)
    - [Weakness Detecability](#weakness-detecability)
    - [Technical Impact](#technical-impact)
    - [Fixes](#fixes)
  - [2. Command Injection](#2-command-injection)
    - [Exploitability](#exploitability-1)
    - [Weakness Prevalence](#weakness-prevalence-1)
    - [Weakness Detecability](#weakness-detecability-1)
    - [Technical Impact](#technical-impact-1)
    - [Fixes](#fixes-1)
  - [3. CRSF](#3-crsf)
    - [Exploitability](#exploitability-2)
    - [Weakness Prevalence](#weakness-prevalence-2)
    - [Weakness Detecability](#weakness-detecability-2)
    - [Technical Impact](#technical-impact-2)
    - [Fixes](#fixes-2)
  - [4. SQL Injection](#4-sql-injection)
    - [Exploitability](#exploitability-3)
    - [Weakness Prevalence](#weakness-prevalence-3)
    - [Weakness Detecability](#weakness-detecability-3)
    - [Technical Impact](#technical-impact-3)
    - [Fixes](#fixes-3)
  - [5. CSP (Content Security Policy) Bypass](#5-csp-content-security-policy-bypass)
    - [Exploitability](#exploitability-4)
    - [Weakness Prevalence](#weakness-prevalence-4)
    - [Weakness Detecability](#weakness-detecability-4)
    - [Technical Impact](#technical-impact-4)
    - [Fixes](#fixes-4)
  - [6. XSS (Cross-site scripting)](#6-xss-cross-site-scripting)
    - [Exploitability](#exploitability-5)
    - [Weakness Prevalence](#weakness-prevalence-5)
    - [Weakness Detecability](#weakness-detecability-5)
    - [Technical Impact](#technical-impact-5)
    - [Fixes](#fixes-5)
  - [7. Weak Session IDs](#7-weak-session-ids)
    - [Exploitability](#exploitability-6)
    - [Weakness Prevalence](#weakness-prevalence-6)
    - [Weakness Detecability](#weakness-detecability-6)
    - [Technical Impact](#technical-impact-6)
    - [Fixes](#fixes-6)
  - [8. Javascript](#8-javascript)
    - [Exploitability](#exploitability-7)
    - [Weakness Prevalence](#weakness-prevalence-7)
    - [Weakness Detecability](#weakness-detecability-7)
    - [Technical Impact](#technical-impact-7)
    - [Fixes](#fixes-7)
  - [9. File Upload](#9-file-upload)
    - [Exploitability](#exploitability-8)
    - [Weakness Prevalence](#weakness-prevalence-8)
    - [Weakness Detecability](#weakness-detecability-8)
    - [Technical Impact](#technical-impact-8)
    - [Fixes](#fixes-8)

# How to start DVWA

Just use `docker-compose.yaml` from this folder. Then run

```
docker compose up -d
```

# Instructions

For each vulnerability, suggest/show a fix for it. If it is a threat (cannot be fixed), please suggest a mitigation methodology. Please **highlight/explain** the concept clearly.

# Vulnerabilities

## 1. Bruce Force

| Exploitability | Weakness Prevalence | Weakness Detecability | Technical Impact |
| :------------: | :-----------------: | :-------------------: | :--------------: |
|  Average (2)   |   Widespread (3)    |       Easy (3)        |   Moderate (2)   |

URL: [http://localhost:8080/vulnerabilities/brute/](http://localhost:8080/vulnerabilities/brute/)

???????????????????????????????????? password ??????????????????????????????????????? username ??????????????????????????????????????????????????????????????????????????????????????????????????????????????? password ??????????????????????????????????????? ??? ????????????????????? login ??????????????????????????????????????????????????????????????????????????????

![](./assets/bruce-force.png)

### Exploitability

??????????????????????????? bruce force ???????????????????????????????????????????????????????????? ????????????????????????????????????????????? effort ?????????????????????????????????????????????????????? script ???????????????????????? hacker ???????????????????????????????????????????????????????????? login ???????????????????????????????????????????????????

### Weakness Prevalence

???????????? vulnerability ???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????? ???????????????????????????????????????????????????????????? login ?????????????????? username ????????? password ???????????????????????? CAPTCHA ???????????? 2FA ??????????????????????????? attempt limitation

### Weakness Detecability

?????????????????????????????????????????? ??????????????????????????? login ????????????????????????????????????????????????????????? ??? ??????????????????????????????????????????????????????????????? ?????????????????????????????????????????????????????? brute force ?????????

### Technical Impact

????????????????????????????????????????????? ????????????????????????????????? hacker ??????????????????????????????????????????????????????????????? admin ????????? ???????????????????????????????????????????????????????????????????????????????????????????????????

### Fixes

- ????????? CAPTCHA ???????????? 2FA ?????????????????????????????????????????? login ?????????????????????????????????
- ???????????????????????????????????????????????????????????? login ?????????????????????????????????????????? user ?????????????????????????????????????????????????????????????????????????????????

## 2. Command Injection

| Exploitability | Weakness Prevalence | Weakness Detecability | Technical Impact |
| :------------: | :-----------------: | :-------------------: | :--------------: |
|  Average (2)   |    Uncommon (1)     |      Average (2)      |    Severe (3)    |

URL: [http://localhost:8080/vulnerabilities/exec/#](http://localhost:8080/vulnerabilities/exec/#)

??????????????????????????? command ???????????? input ?????? website ??????????????????????????? server ???????????? server ??????????????? command ?????????????????? execute ????????? ??? ??????????????????????????????????????????????????????

![](./assets/command-injection.png)

### Exploitability

???????????????????????????????????? exploit ?????????????????????????????????????????????????????? ??????????????????????????? hacker ????????????????????????????????????????????????????????? linux command ????????????????????????

### Weakness Prevalence

???????????? vulnerability ???????????????????????????????????????????????????????????? ?????????????????????????????????????????????????????? library ??????????????? execute command ????????????????????????????????????????????? input ????????????????????????????????????????????? ??????????????????????????????????????????????????? website ??????????????????????????????????????? ???????????? website ???????????????????????????????????? library ????????????????????????????????????????????? input

### Weakness Detecability

??????????????????????????????????????????????????????????????? client-side source code ??????????????? command ????????????????????? execute ????????? server ?????????????????????????????????????????????????????????????????????????????? vulnerability ????????????????????? ???????????????????????????????????? basic linux command ??????????????? server ?????????????????? response

### Technical Impact

?????????????????????????????? ?????????????????????????????????????????? hacker ????????????????????? server ?????????????????????????????????????????? ???????????????????????? hacker ???????????????????????????????????????????????????????????????????????????????????? ?????????????????????????????? SSH Public key ?????????????????????????????????????????????????????????????????? server ???????????????????????? hacker ??????????????? login ???????????? server ????????? ??? ????????? ????????????????????????????????????????????????????????? malware ??????????????? server ???????????????

### Fixes

- ?????????????????????????????? `exec` / `eval` ????????? ??? ???????????????????????????????????????????????? library ??????????????????????????????????????????????????????????????????????????? input ?????????????????????
- validate input ???????????????????????? ????????????????????????????????????????????????????????? ??????????????????????????? whitelist ???????????? blacklist ??????????????? ??????????????????????????????????????????????????????????????????????????? ??????????????????????????????????????? whitelist ????????? ???????????? Regex

## 3. CRSF

| Exploitability | Weakness Prevalence | Weakness Detecability | Technical Impact |
| :------------: | :-----------------: | :-------------------: | :--------------: |
|    Easy (3)    |    Uncommon (1)     |       Easy (3)        |   Moderate (2)   |

URL: [http://localhost:8080/vulnerabilities/csrf/?password_new=password&password_conf=password&Change=Change#](http://localhost:8080/vulnerabilities/csrf/?password_new=password&password_conf=password&Change=Change#)

??????????????????????????? DVWA ?????????????????????????????????????????? URL ??????????????????????????????????????????????????? password ????????? `http://localhost:8080/vulnerabilities/csrf/?password_new=password&password_conf=password&Change=Change#` ??????????????????????????????????????????????????????????????? URL ??????????????? parameter ???????????????????????????????????????????????????????????????????????????????????????????????????????????? ??????????????????????????????????????????????????? password ????????????????????????????????????????????????????????????????????????

### Exploitability

????????? exploit vulnerability ???????????????????????????????????????????????? ????????????????????????????????????????????????????????? URL query parameters ????????????????????????

### Weakness Prevalence

????????????????????????????????????????????????????????? ????????????????????????????????? OAuth ??????????????????????????????????????????????????? ?????????????????????????????????????????????????????????????????????????????? implement ???????????? login / forgot password ???????????????????????????

### Weakness Detecability

?????????????????????????????????????????? ?????????????????????????????????????????? URL ?????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????

### Technical Impact

????????????????????????????????????????????? ?????????????????????????????????????????????????????????????????????????????? admin ????????????????????? hacker ?????????????????????????????????????????????????????????????????????????????????????????????????????????

### Fixes

- ?????????????????????????????? input ????????? query parameters
- ??????????????????????????????????????? current password ???????????????????????????????????? confirm ??????????????????????????????????????????????????? password ???????????? ???
- ????????? CSRF Token ????????????????????????????????????????????? request ?????????????????????????????????????????????????????????????????? request ????????????????????????????????????????????????????????? ??? ?????????????????????

## 4. SQL Injection

| Exploitability | Weakness Prevalence | Weakness Detecability | Technical Impact |
| :------------: | :-----------------: | :-------------------: | :--------------: |
|  Average (2)   |   widespread (3)    |      Average (2)      |   Servere (3)    |

URL: [http://localhost:8080/vulnerabilities/sqli/?id=%27+OR+1%3D1%3B+--+&Submit=Submit#](http://localhost:8080/vulnerabilities/sqli/?id=%27+OR+1%3D1%3B+--+&Submit=Submit#)

?????????????????????????????? hacker ??????????????????????????? SQL command ???????????? input ????????? web application ?????????????????????????????????????????????????????????????????????????????? ???????????????????????????????????????????????????????????????????????????, ?????????????????????????????????????????????????????????, ?????????????????????????????????????????????????????????????????????

??????????????????????????????????????????????????? ?????????????????? `' OR 1=1; -- ` ???????????????????????? input

![](./assets/sql-injection.png)

### Exploitability

????????? exploit vulnerability ??????????????????????????????????????????????????????????????? ??????????????????????????? hacker ????????????????????????????????????????????????????????? developer implement input ?????????????????????????????? ????????? hacker ????????????????????????????????????????????? SQL ?????????????????????????????????????????????

### Weakness Prevalence

???????????????????????????????????????????????????????????????????????????????????????????????????????????? ??????????????????????????? server program ?????????????????????????????? execute SQL command ?????????????????? ????????????????????????????????? validate input ?????????????????????????????????????????????????????????

### Weakness Detecability

??????????????????????????????????????????????????????????????? ??????????????????????????? code ????????????????????????????????????????????????????????????????????????????????? server ???????????? hacker ??????????????????????????? exploit ??????????????????????????????

### Technical Impact

????????????????????????????????????????????? ?????????????????????????????????????????????????????????????????????????????? Database backup ????????? ??????????????????????????????????????? hacker drop database ??????????????????????????????????????????????????????????????????????????????????????????

### Fixes

- ????????? ORM (Object-relational mapping) ????????????????????????????????? SQL command ?????????????????????????????? ??????????????????????????????????????? library ???????????????????????? develop ??????????????????????????????????????????????????????????????????????????????
- ??????????????? validate input ??????????????????????????????????????????????????????????????????????????????

## 5. CSP (Content Security Policy) Bypass

| Exploitability | Weakness Prevalence | Weakness Detecability | Technical Impact |
| :------------: | :-----------------: | :-------------------: | :--------------: |
| Difficult (1)  |    Uncommon (1)     |      Average (2)      |    Minor (1)     |

URL: [http://localhost:8080/vulnerabilities/csp/](http://localhost:8080/vulnerabilities/csp/)

?????????????????????????????? developer ????????????????????????????????? hacker ?????????????????????????????? script ??????????????????????????????????????????????????? website ????????? ??????????????????????????????????????????????????????????????????????????? javascript ?????????????????????????????? website ???????????? input

![](./assets/csp-bypass.png)

### Exploitability

?????????????????????????????????????????????????????????????????? ??????????????????????????? hacker ??????????????????????????? effort ????????????????????????????????????????????? script ??????????????? load ???????????? website ????????????????????????

### Weakness Prevalence

??????????????????????????? ???????????????????????? website ????????????????????????????????????????????????????????????????????????????????? load script ???????????????????????????????????? user ????????????????????????????????????????????????

### Weakness Detecability

??????????????????????????????????????????????????????????????? hacker ???????????????????????????????????????????????????????????????????????? developer ????????????????????????????????? load script ??????????????????????????????????????????

### Technical Impact

?????????????????????????????????????????? ??????????????????????????? script ????????????????????????????????????????????? browser ????????? hacker ???????????????????????? ??????????????????????????? developer ???????????? external script ??????????????????????????? server ????????????

### Fixes

- ?????????????????????????????? user ?????????????????? load external script ?????????

## 6. XSS (Cross-site scripting)

| Exploitability | Weakness Prevalence | Weakness Detecability | Technical Impact |
| :------------: | :-----------------: | :-------------------: | :--------------: |
|  Average (2)   |   Widespread (3)    |      Average (2)      |   Moderate (2)   |

URL: [http://localhost:8080/vulnerabilities/xss_d/?default=English%3Cscript%3Ealert(%27hacked%27)%3C/script%3E](<http://localhost:8080/vulnerabilities/xss_d/?default=English%3Cscript%3Ealert(%27hacked%27)%3C/script%3E>)

?????????????????????????????? input ????????? hacker ?????? javascript ?????????????????????????????? ????????????????????????????????? browser execute script ??????????????????????????? ????????? script ????????????????????????????????????????????????????????????????????????????????????????????? hacker ??????????????????????????????????????? ???????????? ????????????????????????????????????????????????????????????????????? user ?????????????????????????????????????????????????????????????????? hacker

![](./assets/xss-dom.png)

### Exploitability

????????? exploit vulnerability ??????????????????????????????????????????????????????????????? ??????????????????????????? hacker ??????????????????????????????????????????????????????????????? ??????????????? script ???????????????????????? ??????????????????????????? script ?????????????????????????????? ??????????????????????????? hacker ????????????????????????????????????????????????????????? script ??????????????????????????????????????????????????????????????????????????? browser ??????????????????????????????????????????

### Weakness Prevalence

???????????????????????????????????????????????????????????????????????????????????????????????????????????? ??????????????????????????? developer ???????????????????????? escape ???????????????????????????????????????????????????????????????????????????????????? HTML ???????????? ???????????? <, >, &, " ????????? ' ?????????????????????????????????????????????????????????????????? hacker ??????????????????????????? XSS ?????????

### Weakness Detecability

???????????????????????????????????? ???????????????????????????????????????????????? source code ?????????????????????????????? ???????????????????????????????????????????????? exploit ??????

### Technical Impact

????????????????????????????????????????????????????????????????????? ??????????????????????????????????????????????????????????????????????????????????????????????????? ??????????????????????????????????????????????????? end user ?????????????????????

### Fixes

- ???????????????????????? escape string ???????????????????????????????????????????????? input ??????
- ????????? Framework / Library ???????????????????????????????????????????????? ??????????????????????????????????????? security issue ????????????????????????

## 7. Weak Session IDs

| Exploitability | Weakness Prevalence | Weakness Detecability | Technical Impact |
| :------------: | :-----------------: | :-------------------: | :--------------: |
|    Easy (3)    |    Uncommon (1)     |       Easy (3)        |   Moderate (2)   |

URL: [http://localhost:8080/vulnerabilities/weak_id/](http://localhost:8080/vulnerabilities/weak_id/)

?????????????????????????????? session id ???????????????????????????????????????????????? ???????????? hacker ????????????????????? session id ??????????????????????????????????????? ???????????????????????????????????????????????? ?????????????????????????????????????????????

### Exploitability

???????????????????????????????????? ?????????????????????????????????????????????????????????????????????????????? cookie ??????????????????????????? session id ???????????????????????????????????? ????????????????????????????????? set session id ?????????????????????????????????????????????????????????

### Weakness Prevalence

???????????????????????????????????????????????? ??????????????????????????? developer ???????????????????????? session id ????????? random ??????????????????????????? ???????????????????????????????????????????????? session id ????????????????????? ?????????????????????????????????????????? ????????????????????????????????????????????????

### Weakness Detecability

??????????????????????????????????????? ?????????????????????????????? cookie ????????? browser ???????????????????????????????????????

### Technical Impact

??????????????????????????????????????????????????????????????????????????????????????? ??????????????????????????????????????????????????????????????????????????????????????????????????? ??????????????????????????????????????????????????? end user ?????????????????????

### Fixes

- ????????? session id ????????? random ??????????????????????????? ???????????????????????????????????????????????????

## 8. Javascript

| Exploitability | Weakness Prevalence | Weakness Detecability | Technical Impact |
| :------------: | :-----------------: | :-------------------: | :--------------: |
| Difficult (1)  |     Common (2)      |     Difficult (1)     |    Minor (1)     |

URL: [http://localhost:8080/vulnerabilities/javascript/](http://localhost:8080/vulnerabilities/javascript/)

?????????????????????????????? javascript function ????????? developer ?????????????????????????????????????????????????????? ??????????????? bypass ???????????????????????? ????????????????????? javascript ??????????????? execute ??????????????????????????????????????????????????????????????????

![](./assets/javascript.png)

### Exploitability

????????????????????????????????? ??????????????????????????? hacker ??????????????????????????????????????????????????????????????????????????? source code ????????? website ????????????

### Weakness Prevalence

????????????????????????????????? ??????????????????????????????????????????????????????????????????????????? hacker ??????????????????????????? function ????????? developer ?????????????????????????????? website

### Weakness Detecability

????????????????????????????????? ??????????????????????????? hacker ??????????????????????????????????????????????????????????????????????????? source code ????????? website ????????????

### Technical Impact

???????????????????????? ???????????????????????????????????????????????????????????? hacker ?????????????????????????????????????????????????????? ?????????????????????????????????????????? developer ????????????????????? code ???????????????

### Fixes

- ????????????????????????????????????????????????????????? 100% ?????????????????????????????????????????????????????????????????????????????????????????? source code ????????? website ?????????
- ??????????????????????????? parser ????????????????????????????????????????????????????????? ???????????????????????? complied code ?????????????????????????????????????????? ????????????????????????????????? hacker ???????????????????????????????????? code ??????????????????????????????????????????

## 9. File Upload

| Exploitability | Weakness Prevalence | Weakness Detecability | Technical Impact |
| :------------: | :-----------------: | :-------------------: | :--------------: |
|  Average (2)   |     Common (2)      |       Easy (3)        |   Moderate (2)   |

URL: [http://localhost:8080/vulnerabilities/upload/](http://localhost:8080/vulnerabilities/upload/)

upload `index.php`

```php
<?php phpinfo(); ?>
```

????????????????????? upload script file ?????????????????? ????????????????????????????????????????????? upload ????????????????????? video ????????????????????????????????????????????? script ????????????????????????????????????????????????????????? ??????????????????????????? script ????????????????????? execute ??????????????? ???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????

URL: [http://localhost:8080/hackable/uploads/index.php](http://localhost:8080/hackable/uploads/index.php)

![](./assets/file-upload.png)

### Exploitability

hacker ????????????????????? effort ??????????????????????????????????????????????????????????????? script ?????????????????????????????????????????????????????????????????????????????????????????????????????????????????? developer

### Weakness Prevalence

??????????????????????????????????????????????????? ??????????????? developer ???????????????????????????????????? check file type ?????????????????? backend

### Weakness Detecability

???????????????????????????????????? ???????????????????????????????????????????????????????????????????????????????????? check file type ????????????????????? restrict file type ??????????????????????????????????????? DOM ????????????????????? upload ???????????????????????????

### Technical Impact

???????????????????????????????????? ????????????????????????????????? execute script ????????? hacker ??????????????? ????????????????????? hacker ?????????????????????????????????????????????????????????

### Fixes

- ?????????????????? validate input ??????????????????????????????????????? script ??????????????????????????????????????????????????????
- ???????????????????????? file type ????????????????????????????????? image ?????????????????????
- ??????????????? metadata ????????? file ????????????????????? file ???????????????????????????????????????????????????
