import re

def serhHost(strg):   #функция поиску hostName на основании списка шаблонов
    hostList = list()
    for patn in patnHost:  # перебираем регулярные выражения Host
        host = re.search(patn, strg)  # осуществляем поиск строках значения соответствющим рег. выражениям Host
        print(host)
        if host is not None:  # осуществляем проверку не пустых полученных значений
            hostList.append(host[0])   #добавляем найденный hostname в список
    print(hostList)
    if len(hostList):   #если список не пустой
        host = hostList[-1]   #с целью избежания некорректного найденного шаблона отправляем последний найденный hostName (проблема UAK6-CR4-B - M7-CR9-A)
        if host in listHostExcn:
            return False
        else: return host

patnHost = [    #список регулярных выражений для поиска HostName. Шаблоны располагаются по воссрастанию количества символов. Решение проблемы UAK6-CR4-B - M7-CR9-A
    '\b[A-Z]\d-[A-Z]{2}\d\b',   #6 M7-AR3
    '\b[A-Z]{3}-[A-Z]{2}\d\b',   #7 MRK-AR1
    '\b[A-Z]{4}-[A-Z]{2}\b',   #7 ALIC-AR
    '\b[A-Z]{3}-[A-Z]{2}\d\b',   #7 BMK-AR1
    '\b[A-Z]{3}\d-[A-Z]\d\b',   #7 UAK9-R1
    '\b[A-Z]{2}\d-[A-Z]{3}\b',   #7 HX0-GRZ
    '\b[A-Z]\d-[A-Z]{2}\d{2}\b',  #7 M7-AR10
    '\b[A-Z]\d-[A-Z]{3}\d\b',   #7 M7-ASW1
    '\b[A-Z]\d{2}-[A-Z]{2}\d\b',   #7 M10-AR2
    '\b[A-Z]\d-[A-Z]{2}\d-[A-Z]\b',  #8 M7-CR9-A
    '\b[A-Z]{4}-[A-Z]{2}\d\b',  #8 FRKT-CR5
    '\b[A-Z]{3}\d{2}-[A-Z]\d\b',   #8 UAK10-R1
    '\b[A-Z]\d{2}-[A-Z]{3}\d\b',   #8 M10-ASW3
    '\b[A-Z]{3}-[A-Z]{3}\d\b',   #8 IGN-CON1
    '\b[A-Z]{3}\d-[A-Z]{2}\d\b',   #8 UAK8-SR2
    '\b[A-Z]{3}\d-[A-Z]\d{2}\b',   #8 CXK6-A23
    '\b[A-Z]{3}\d-[A-Z]{3}\b',   #8 CXK6-PVL
    '\b[A-Z]\d-[A-Z]{4}\d\b',   #8 M7-ASTK1
    '\b[A-Z]\d-[A-Z]{3}\d{2}\b',   #8 M7-ASW10
    '\b[A-Z]\d{2}-[A-Z]{2}\d{2}\b',   #8 M10-AR10
    '\b[a-z]{3}-[a-z]{3}\d\b',   #8 ufa-rgr2
    '\b[a-z]{3}\d-[a-z]{2}\d\b',   #8 uak7-ar1
    '\b[A-Z]{4}-[A-Z]{3}\d\b',  #9 KLNG-RGR4
    '\b[A-Z]{3}\d-[A-Z]{3}\d\b',   #9 UAK6-CON3
    '\b[A-Z]{3}-[A-Z]{2}-[A-Z]\d\b',   #9 AST-CR-R1
    '\b[A-Z]{3}\d-[A-Z]{3}\d\b',   #9 UAK8-RGR1
    '\b[A-Z]{3}\d{2}-[A-Z]{2}\d\b',   #9 UAK10-SR2
    '\b[A-Z]{3}\d-[A-Z]{3}\d\b',   #9 UAK1-SSW6
    '\b[A-Z]{3}\d-[A-Z]{3}\d\b',   #9 UAK9-ASW1
    '\b[A-Z]{4}-[A-Z]{2}\d{2}\b',   #9 VLDK-SW12
    '\b[A-Z]{5}-[A-Z]{2}\d\b',   #9 BRVSK-AR1
    '\b[A-Z]{4}-[A-Z]{2}\d{2}\b',   #9 IVNV-AR23
    '\b[A-Z]{2}\d-[A-Z]{3}\d{2}\b', #9 HR0-ATS43
    '\b[A-Z]{3}\d-[A-Z]{4}\b',   #9 CXK6-NVOR
    '\b[A-Z]{4}-[A-Z]{2}\d{2}\b',   #9 MSCW-AR14
    '\b[A-Z]{3}\d-[A-Z]{2}-[A-Z]\b',   #9 UAK1-CR-A
    '\b[A-Z]{3}-[A-Z]{4}\d\b',   #9 GCU-SSTK1
    '\b[A-Z]{3}-[A-Z]{3}\d{2}\b',   #9 GCU-ASW14
    '\b[A-Z]\d{2}-[A-Z]{4}\d\b',   #9 M10-ASTK1
    '\b[A-Z]\d{2}-[A-Z]{3}\d{2}\b',   #9 M10-ASW10
    '\b[A-Z]\d{2}-[A-Z]{2}\d-[A-Z]\b',   #9 M10-CR7-B
    '\b[a-z]{3}\d-[a-z]{3}\d\b',   #9 uak7-con1
    '\b[a-z]{4}-[a-z]{3}\d\b',   #9 kirv-bpe3
    '\b[a-z]{3}\d-[a-z]{2}-[a-z]\b',   #9 uak7-cr-a
    '\b[A-Z]{3}\d-[A-Z]{2}\d-[A-B]\b',  # 10 UAK6-CR4-B
    '\b[A-Z]{4}-[A-Z]{4}\d\b',   #10 IZHK-BRAS1
    '\b[A-Z]{4}-[A-Z]{3}\d{2}\b',   #10 NNOV-BPE21
    '\b[A-Z]{4}-[A-Z]{2}\d-[A-Z]\b',   #10 SPBR-CR4-A
    '\b\d{2}-[A-Z]{3}-[A-Z]{2}\d\b',   #10 23-NVP-AR1
    '\b[A-Z]{3}\d{2}-[A-Z]{3}\d\b',    #10 UAK10-ASW1
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]\d\b',   #10 KLM-YSK-R1
    '\b[A-Z]{3}\d-[A-Z]{4}\d\b',   #10 UAK5-SSTK1
    '\b[A-Z]{4}-[A-Z]{2}\d-\d\b',   #10 VLDK-SW5-2
    '\b[A-Z]{4}-[A-Z]{2}\d{3}\b',   #10 VLMR-DR001
    '\b[A-Z]{3}-[A-Z]\d-[A-Z]{2}\d\b',  #10 UFA-N2-AR1
    '\b[a-z]{4}-[a-z]{3}\d{2}\b',   #10 kirv-rgr11
    '\b[a-z]{4}-[a-z]{2}\d-[a-z]\b',   #10 smra-cr5-a
    '\b[A-Z]{4}\d{2}-[A-Z]{2}\d\b',   #10 YSLV21-DR1
    '\b[A-Z]\d-[A-Z]{3}-[A-Z]{2}\d\b',   #10 M7-DPC-SW1
    '\b[A-Z]\d{2}-[A-Z]{5}\d\b',   #10 M10-VTARA4
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]{2}\d\b',   #11 MRK-LTC-AR1
    '\b[A-Z]{4}-[A-Z]{4}\d{2}\b',   #11 SRSK-BRAS11
    '\b\d{2}-[A-Z]{3}-[A-Z]{3}\d\b',   #11 13-ARD-CON1
    '\b\d{2}-[A-Z]{4}-[A-Z]{2}\d\b',   #11 11-EMVA-AR1
    '\b[A-Z]{3}\d{2}-[A-Z]{3}\d{2}\b',   #11 UAK10-ESR13
    '\b[A-Z]{3}-[A-Z]{2}-[A-Z]{3}\d\b',   #11 AST-CR-BPE1
    '\b[A-Z]{3}-[A-Z]{2}-[A-Z]{2}-\d\b',   #11 DGS-BB-MX-1
    '\b[A-Z]{4}-[A-Z]{3}-[A-Z]\d\b',   #11 NVSK-DPC-R1
    '\b[A-Z]{4}-[A-Z]{3}\d{3}\b',   #11 VLDK-ASW117
    '\b[A-Z]{4}-\d{2}-[A-Z]{2}\d\b',   #11 MCEN-39-AR1
    '\b[A-Z]{3}\d{2}-[A-Z]{2}\d-[A-Z]\b',   #11 UAK10-CR5-A
    '\b[A-Z]{3}\d-[A-Z]{5}\d\b',   #11 UAK1-VTARA
    '\b[A-Z]\d{2}-[A-Z]{3}-[A-Z]{2}\d\b',   #11 M10-DPC-SW1
    '\b[A-Z]{3}-[A-Z]\d{2}-[A-Z]{2}\d\b',   #11 UFA-N10-AR1
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]{3}\d\b',   # 12 BLR-MZG-VGW2
    '\b[A-Z]{4}-[A-Z]{3}-[A-Z]{2}\d\b',   #12 DAVL-LTC-AR1
    '\b[A-Z]{3}-[A-Z]{4}-[A-Z]{2}\d\b',   #12 UFA-CORE-SR2
    '\b[A-Z]{3}-[A-Z]{3}\d-[A-Z]{2}\d\b',   #12 KVL-ATS2-AR1
    '\b[A-Z]\d{2}-[A-Z]{6}\d\b',   #11 [A-Z]\d{2}-[A-Z]{6}\d
    '\b[A-Z]\d{2}-[A-Z]{5}\d{2}\b',   #11 M10-VTARA10
    '\b\d{2}-[A-Z]{5}-[A-Z]{2}\d\b',   #12 35-USTUG-AR1
    '\b\d{2}-[A-Z]{4}-[A-Z]{3}\d\b',   #12 13-ATSH-CON1
    '\b[A-Z]{4}_\d{3}-[A-Z]{2}\d\b',    #12 ZHRD_355-DR1
    '\b[A-Z]{4}-[A-Z]{3}\d{4}\b',   #12 MSCW-ASW1012
    '\b[A-Z]{4}_[A-Z]\d{2}-[A-Z]{2}\d\b',   #12 SMLK_A27-DR1
    '\b[A-Z]\d{2}[A-Z]{5}-[A-Z]{2}\d\b',   #12 M10TMGUS-AR1
    '\b[A-Z]{3}-[A-Z]{3}-\d{2}[A-Z]\d\b',   #12 SVO-VLK-25P1
    '\b[a-z]{3}-[a-z]{4}-[a-z]{2}\d\b',   #12 bor-cats-ar1
    '\b[A-Z]{4}-[A-Z]{3}\d{2}-[A-Z]{2}\b',   #13 CHEB-ATS55-DR
    '\b[A-Z]{4}-[A-Z]{4}-[A-Z]{2}\d\b',   #13 PNZA-CORE-DR1
    '\b[A-Z]{4}-[A-Z]{3}\d-[A-Z]{2}\d\b',   #13 NOVK-ATS7-AR1
    '\b[A-Z]{4}-[A-Z]{3}-[A-Z]{3}\d\b',   #13 CHKM-LTC-VGW2
    '\b[A-Z]{3}-[A-Z]{4}-[A-Z]{2}\d{2}\b',   #13 UFA-CORE-AR11
    '\b[A-Z]{3}-[A-Z]{4}-[A-Z]{3}\d\b',   #13 UFA-CORE-BPE2
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]{2}-[A-Z]\d\b',   #13 VLG-KTL-CS-R0
    '\b[A-Z]{3}-[A-Z]{3}-\d{2}-[A-Z]\d\b',   #13 SVO-CHI-03-P1
    '\b\d{2}-[A-Z]{3}-\d{2}-[A-Z]{2}\d\b',   #13 23-KRA-24-AR1
    '\b[A-Z]{3}-[A-Z]{3}-\d{2}-[A-Z]\d\b',   #13 SVO-ARD-03-P1
    '\b[A-Z]{3}-[A-Z]{2}-\d{3}-[A-Z]\d\b',   #13 AST-AS-025-R1
    '\b[A-Z]{3}-[A-Z]{2}-[A-Z]{3}-[A-Z]\d\b',  #13 AST-AS-BHT-R1
    '\b[A-Z]{3}-[A-Z]{3}-\d{2}-[A-Z]\d\b',   #13 SVO-BES-03-P1
    '\b\d{2}-[A-Z]{4}\d{2}-[A-Z]{2}\d\b',   #13 35-VLGD27-AR1
    '\b\d{2}-[A-Z]{4}\d-[A-Z]{3}\d\b',   #13 13-KVLA2-CON1
    '\b[A-Z]{4}_\d{4}-[A-Z]{2}\d\b',   #13 UVRV_5840-DR1
    '\b[A-Z]{4}-[A-Z]{3}-[A-Z]{2}\d{2}\b',   #13 EBRG-DPC-SW10
    '\b[A-Z]{4}-[A-Z]{2}\d{2}-[A-Z]{2}\d\b',   #13 ZLND-UD03-AR1
    '\b[A-Z]{4}-[A-Z]{3}-[A-Z]{2}\d\b',  #13 KRDL-LTC-AR1
    '\b[A-Z]{4}_\d{4}-[A-Z]{2}\d\b',   #13 ZNAM_5223-DR1
    '\b[A-Z]{4}-[A-Z]{3}-[A-Z]{2}\d{2}\b',   #13 EBRG-DPC-SW10
    '\b[A-Z]\d{2}[A-Z]{5}-[A-Z]{3}\d\b',   #13 M10TMGUS-ASW1
    '\b[a-z]{2}\d-[a-z]{3}-[a-z]{3}\d{2}\b',   #13 pe2-lab-ats66
    '\b[a-z]{4}-[a-z]{3}-[a-z]{3}\d\b',   #13 yosh-gts-con1s
    '\b[a-z]{4}-[a-z]{4}-[a-z]{2}\d\b',   #13 nnov-nmts-cr9
    '\b[a-z]{4}-[a-z]{3}\d-[a-z]{2}\d\b',   #13 sarv-ats3-ar2
    '\b[a-z]{4}-[a-z]{4}-[a-z]{2}\d\b',   #13 nnov-nmts-cr7
    '\b[a-z]{3}-[a-z]{4}-[a-z]{3}\d\b',   #13 bor-cats-con1
    '\b[A-Z]{4}-[A-Z]{3}\d{2}-[A-Z]{2}\d\b',  #14 TLTT-ATS22-SR1
    '\b[A-Z]{4}-[A-Z]{4}-[A-Z]{3}\d\b',    #14 SMRA-AMTS-BPE1
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]{4}\d{2}\b',   #14 BLB-LTC-BRAS17
    '\b[A-Z]{4}-[A-Z]{2}\d{3}-[A-Z]{2}\d\b',   #14 SZRN-PS901-AR1
    '\b[A-Z]{4}-[A-Z]{4}\d-[A-Z]{2}\d\b',   #14 SMRA-OPTS3-AR1
    '\b[A-Z]{3}-[A-Z]{2}-[A-Z]\d-[A-Z]{2}\d{2}\b',   #14 KCR-UD-R1-MX80
    '\b\d{2}-[A-Z]{4}\d{3}-[A-Z]{2}\d\b',   #14 78-SPBR343-DR1
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]{3}-[A-Z]\d\b',   #14 VLG-SAH-KSL-R0
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]-[A-Z]{2}\d{2}\b',   #14 'KRD-KMK-P-MX48
    '\b[A-Z]{3}-[A-Z]{4}-\d{2}-[A-Z]\d\b',   #14 SVO-PAVL-01-P1
    '\b[A-Z]{3}-[A-Z]{3}-\d{3}-[A-Z]\d\b',   #14 KBR-NLK-096-R1
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]{3}-[A-Z]\d\b',   #14 SVO-VLK-HOL-P1
    '\b[A-Z]{3}-[A-Z]{5}\d-[A-Z]{2}\d\b',   #14 UNI-OTMUS2-AR1
    '\b[A-Z]{4}-[A-Z]{3}\d{2}-[A-Z]{3}\b',   #14 CHEB-ATS55-BPE
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]{2}-[A-Z]{2}\d\b',   #14 SVO-VLK-CR-RR2
    '\b[A-Z]{4}_[A-Z]{3}\d{2}-[A-Z]{2}\d\b',   #14 BLGD_ATS21-DR1
    '\b\d{4}_\d{3}_[A-Z]{2}\d{2}[A-Z]\b',   #14 7609_236_AR75A
    '\b[A-Z]{4}-[A-Z]{5}-[A-Z]{2}\d\b',   #14 RZAN-KRBLN-DR1
    '\b[A-Z]{4}_[A-Z]\d{2}-[A-Z]{4}\d\b',   #14 LPTZ_A22-ASBR1
    '\b[A-Z]{4}_[A-Z]{3}-[A-Z]{4}\d\b',   #14 LPTZ_MTS-BRAS1
    '\b[A-Z]{4}-[A-Z]{2}\d-[A-Z]{2}\d{3}\b',   #14 CHRK-AR1-MX480
    '\b[A-Z]{3}-[A-Z]{2}-[A-Z]{4}-[A-Z]\d\b',   #14 AST-CR-IPOE-R1
    '\b[A-Z]{4}-[A-Z]{3}-[A-Z]{3}\d{2}\b',   #14 NVSK-DPC-SSW11
    '\b[A-Z]{4}_\d{3}-\d-[A-Z]{2}\d\b',   #14 TMBV_247-2-DR1
    '\b[A-Z]{4}-[A-Z]{3}-[A-Z]{4}\d\b',   #14 EBRG-DPC-ASTK1
    '\b[a-z]{4}-[a-z]{3}\d-[a-z]{3}\d\b',   #14 kstv-ats3-con1
    '\b[a-z]{4}-[a-z]{3}\d{2}-[a-z]{2}\d\b',   #14 dzer-ats21-ar1
    '\b[a-z]{4}-[a-z]{4}-[a-z]{3}\d\b',   #14 skls-cats-con1
    '\b[A-Z]{4}-[A-Z]{6}-[A-Z]{2}\d\b',     #15 VLZS-BEREZA-AR1
    '\b[A-Z]{3}-[A-Z]{4}-[A-Z]{4}\d{2}\b',   #15 UFA-CORE-BRAS21
    '\b[A-Z]{3}-[A-Z]{4}-[A-Z]{3}\d-[A-Z]\b',   #15 UFA-CORE-VGW3-R
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]{4}-[A-Z]\d\b',   #15 VLG-VOL-MGOR-R0
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]-[A-Z]{2}\d{3}\b',  # 15 KRD-KOR-P-MX480
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]\d-[A-Z]{2}\d{2}\b',  # 15 KCR-ADH-R1-MX80
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]-[A-Z]{2}\d{3}\b',  # 15 KRD-ARM-P-MX480
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]{3}\d-[A-Z]\d\b',  # 15 VLG-VOL-BAT3-R0
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]{2}\d{2}-[A-Z]\d\b',   #15 VLG-KAL-PS35-R0
    '\b[A-Z]{4}-[A-Z]{5}\d-[A-Z]{2}\d\b',   #15 ARBZ-OTMUS2-AR1
    '\b[A-Z]{4}-[A-Z]{3}\d{3}-[A-Z]{2}\d\b',   #15 KIRV-PSC408-AR1
    '\b[A-Z]{4}-[A-Z]{5}\d-[A-Z]{2}\d\b',   #15 SUNA-OTMUS3-AR2
    '\b[A-Z]{2}\d{2}-\d[A-Z]{2}\d{2}-[A-Z]{4}\b',   #15 MX80-1AG45-BALT
    '\b[A-Z]{3}-[A-Z]{3}-\d{3}-[A-Z]{2}\d\b',   #15 'KBR-NLK-040-AS1'
    '\b[A-Z]{4}-[A-Z]{3}\d{2}-[A-Z]{3}\d\b',   #15 KIRV-ATS65-BPE1
    '\b[A-Z]{2}\d{3}-[A-Z]{4}-[A-Z]{4}\b',   #15 MX104-CATS-KRES
    '\b[A-Z]{2}\d{3}-\d[A-Z]{2}\d{3}-[A-Z]{2}\b',   #15 MX104-1AG327-PZ
    '\b[A-Z]{4}_[A-Z]{3}\d{3}-[A-Z]{2}\d\b',   #15 KLGA_ATS253-DR1
    '\b[A-Z]{5}_[A-Z]{3}\d{2}-[A-Z]{2}\d\b',   #15 GUBKN_ATS40-DR1
    '\b[A-Z]{4}-[A-Z]{2}\d{2}-[A-Z]{3}\d{2}\b',   #15 BRAS-ME60-ATS35
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]{3}-[A-Z]{2}\d\b',   #15 KLM-KMS-ART-MX1
    '\b[A-Z]{5}-[A-Z]{3}\d{2}-[A-Z]{2}\d\b',   #15 STOSK-ATS44-DR1
    '\b\d{2}-[A-Z]{4}-[A-Z]{2}\d-[a-z]{2}\d\b',   #15 29-SVDV-DR1-re0
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]{2}-[A-Z]{3}\d\b',   #15 SVO-VLK-CR-BPE1
    '\b[A-Z]{4}-[A-Z]{2}\d{3}[A-Z]-[A-Z]{2}\d\b',   #15 KAZN-PS510B-AR1
    '\b[A-Z]{4}-[A-Z]{2}\d{4}-[A-Z]{2}\d\b',   #15 KAZN-PS5122-AR1
    '\b[A-Z]{4}-[A-Z]{2}\d-\d{2}-[A-Z]{2}\d\b',   #15 NCHL-PS2-02-AR1
    '\b[A-Z]{4}_[A-Z]{6}-[A-Z]{2}\d\b',   #15 BLGD_ATSDUB-DR1
    '\b[A-Z]{3}-[A-Z]{3}-\d{2}-[A-Z]{3}\d\b',   #15 SVO-ALA-02-CON1
    '\b[A-Z]{5}_\d{3}-1-[A-Z]{2}\d\b',   #15 STRTL_271-1-DR1
    '\b[A-Z]{3}-[A-Z]{3}-\d{2}-[A-Z]{3}\d\b',   #15 SVO-OCT-02-CON1
    '\b[A-Z]{4}-[A-Z]{3}\d{2}-\d{4}\b',   #15 CHEB-ATS62-7200
    '\b[a-z]{4}-[a-z]{3}\d{3}-[a-z]{2}\d\b',   #15 nnov-ats342-ar1
    '\b[a-z]{4}-[a-z]{2}\d{4}-[a-z]{2}\d\b',   #15 nnov-ps2251-ar1
    '\b[a-z]{4}-[a-z]{3}\d{2}-[a-z]{3}\d\b',   #15 dzer-ats25-con1
    '\b[A-Z]{3}-[A-Z]{4}-[A-Z]{2}\d-[A-Z]{2}\d\b',  #16 STV-NEVN-PS0-ER1
    '\b[A-Z]{3}-[A-Z]{4}-[A-Z]\d-[A-Z]{2}\d{2}\b',  #16 KCR-UCHK-R1-MX80
    '\b[A-Z]{4}-[A-Z]{3}\d-\d{2}-[A-Z]{2}\d\b',   #16 ORNB-PSE4-16-AR1
    '\b[A-Z]{2}\d{2}-\d[A-Z]{2}\d{3}-[A-Z]{4}\b',   #16 MX80-1AG563-ZAOZ
    '\b[A-Z]{3}-[A-Z]{3}-\d{2}[A-Z]{3}-[A-Z]\d\b',   #16 VLG-VOL-25LET-R0
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]{3}\d{2}-[A-Z]\d\b',   #16 VLG-VOL-RKR37-R0
    '\b[A-Z]{2}\d{2}-\d[A-Z]{2}\d{3}-[A-Z]{4}\b',   #16 MX80-1AG557-APAT
    '\b[a-z]{4}-[a-z]{3}\d{2}-[a-z]{4}\d\b',  #16 pnza-ats52-sorm1
    '\b[A-Z]{2}\d{3}-\d[A-Z]{2}\d{2}-[A-Z]{4}\b',   #16 MX104-1AG56-BGRT
    '\b[A-Z]{2}\d{2}-\d[A-Z]{2}\d{2}-[A-Z]{5}\b',   #16 MX80-1AG39-LOUHI
    '\b[A-Z]{2}\d{3}-\d[A-Z]{2}\d{2}-[A-Z]{4}\b',   #16 MX104-1AG30-SORT
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]{2}-[A-Z]{4}\d\b',   #16 KBR-NLK-CR-BRAS2
    '\b[A-Z]{4}-[A-Z]{3}\d{2}-[A-Z]{3}\d{2}\b',   #16 SRTV-ATS73-BPE11
    '\b[A-Z]{4}-[A-Z]{5}-[A-Z]{4}\d\b',   #16 TLTT-TOTEL-BRAS1
    '\b[A-Z]{2}\d{3}-\d[A-Z]{2}\d{3}-[A-Z]{3}\b',   #16 MX480-1AG210-SPB
    '\b[A-Z]{2}\d{3}-\d[A-Z]{5}-[A-Z]{3}\b',   #16 MX480-1AGMMT-SPB
    '\b[A-Z]{2}\d{3}-\d[A-Z]{2}\d{3}-[A-Z]{3}\b',   #16 MX960-1AG210-SPB
    '\b[A-Z]{2}\d{3}-\d[A-Z]{5}-[A-Z]{3}\b',   #16 MX960-1AGMMT-SPB
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]\d-[A-Z]\d{4}\b',   #16 DAG-BNK-R1-C7206
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]{2}-[A-Z]\d{4}\b',   #16 DAG-MHK-CR-C2851
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]{5}-[A-Z]\d\b',   #16 VLG-PAL-PUTIL-R0
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]\d-[A-Z]\d{4}\b',   #16 DAG-VCH-R1-C2811
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]\d-[A-Z]\d{4}\b',   #16 DAG-TLT-R1-C2811
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]{5}-[A-Z]\d\b',   #16 VLG-KUM-BGORC-R0
    '\b[A-Z]{3}\d-[A-Z]{3}.[A-Z]{3}.[A-Z]{3}\b',   #16 CAR1-GRZ.NET.LOC
    '\b[A-Z]{4}-[A-Z]{2}\d{2}[A-Z]{3}-[A-Z]{2}\d\b',   #16 ULSK-LT95SRV-AR1
    '\b[A-Z]{4}-[A-Z]{4}\d{2}-[A-Z]{4}\b',    #16 TULA-OPTS27-ASBR
    '\b[A-Z]{4}-[A-Z]{2}\d{2}-\d{2}-[A-Z]{2}\d\b',   #16 NCHL-PS18-08-AR1
    '\b[A-Z]{3}\d{3}-[A-Z]{2}\d{3}[A-Z]\d-\d\b',   #16 TMB073-CX600X1-1
    '\b[A-Z]{3}-[A-Z]{4}-[A-Z]{3}\d-[A-Z]{2}\d\b',   #17 STV-KISL-ATS5-ER1
    '\b[A-Z]{4}-[A-Z]{4}\d{3}-[A-Z]{2}\d\b',   #16 KAZN-OPTS512-AR1
    '\b[a-z]{4}-[a-z]{3}\d{3}[a-z]{2}-[a-z]{2}\d\b',   #17 nnov-ats225bg-ar2
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]{3}\d{3}-[A-Z]\d\b',   #17 VLG-VOL-KIR120-R0
    '\b[A-Z]{3}-[A-Z]{3}\d{2}-[A-Z]\d-[A-Z]{2}\d{2}\b',   #17 KCR-ATS25-R1-MX80
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]{4}-[A-Z]-[A-Z]\d\b',   #17 VLG-GOR-KTLB-B-R0
    '\b[A-Z]{2}\d{2}-\d[A-Z]{2}\d{4}-[A-Z]{4}\b',   #17 MX80-1AG6620-BKST
    '\b[A-Z]{4}-[A-Z]{2}\d{2}[A-Z]\d{2}-[A-Z]{3}\d\b',   #17 ULSK-LT95S12-BPE4
    '\b[A-Z]{4}-[A-Z]{2}\d{2}[A-Z]{3}-[A-Z]{3}\d\b',   #17 ULSK-LT95SRV-BPE3
    '\b[A-Z]{2}\d{3}-\d[A-Z]{2}\d{3}-[A-Z]{4}\b',   #17 MX104-1AG440-BRVC
    '\b[a-z]{4}-[a-z]{5}\d{2}-[a-z]{3}\d\b',   #17 yosh-krasn76-con1
    '\b[A-Z]{3}-[A-Z]{4}-[A-Z]{3}\d{2}-[A-Z]{2}\d\b',   #18 STV-PTGR-ATS32-ER1
    '\b[A-Z]{3}-[A-Z]{3}-\d{3}-[A-Z]-[A-Z]{2}\d{2}\b',   #18 KRD-USP-001-P-MX80
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]{3}-[A-Z]-[A-Z]{2}\d{2}\b',  #18 KRD-KRA-KPN-P-MX80
    '\b[A-Z]{3}-[A-Z]{3}-\d{2}-[A-Z]-[A-Z]{2}\d{3}\b',   #18 KRD-KRA-37-P-MX480
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]\d-[A-Z]\d-[A-Z]{2}\d{2}\b',   #18 KRD-SCH-F1-R1-MX80
    '\b[A-Z]{3}-[A-Z]{3}\d{2}-[A-Z]\d-[A-Z]{2}\d{3}\b',   #18 KCR-ATS20-R1-MX480
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]{3}-[A-Z]{2}\d{2}-[A-Z]\b',   #18 KRD-OLG-ORB-MX80-P
    '\b[A-Z]{3}-[A-Z]{3}-\d{2}-[A-Z]\d-[A-Z]{2}\d{2}\b',   #18 KRD-LEN-07-R1-MX80
    '\b[A-Z]{4}-[A-Z]{9}-[A-Z]{2}\d\b',   #18 ZVEN-SHELANGER-AR1
    '\b[A-Z]{2}\d{3}-\d[A-Z]{2}\d{4}-[A-Z]{4}\b',   #18 MX104-1AG5056-KRZM
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]{3}\d{2}-[A-Z]{2}\d{2}\b',   #18 ING-NZR-ATS22-MX80
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]{2}-[A-Z]{3}\d{4}\b',   #18 AST-LIM-CS-ACX2100
    '\b[A-Z]{3}\d[A-Z]-\d-[A-Z]\d{2}.[A-Z]{3}.[A-Z]{2}\b',   #18 ASR1K-1-A52.VSI.RU
    '\b[A-Z]\d{4}-\d-[A-Z]\d{2}.[A-Z]{3}.[A-Z]{2}\b',   #18 C7301-1-A52.VSI.RU
    '\b[A-Z]{4}_[A-Z]{3}\d{3}_\d{2}-[A-Z]{2}\d\b',   #18 KLGA_ATS253_04-AR1
    '\b[A-Z]{2}\d{2}-\d[A-Z]{2}\d{5}-[A-Z]{4}\b',   #18 MX80-1AG79610-SSNV
    '\b[A-Z]{4}-[A-Z]{4}\d.[A-Z]{3}.[A-Z]{3}\b',   #18 KSTR-BRAS4.MSS.KOS
    '\b[A-Z]{3}\d-[A-Z]{3}\d{2}.[A-Z]{3}.[A-Z]{3}\b',   #18 ASR1-ATS22.NET.LOC
    '\b[A-Z]{3}-[A-Z]{3}-\d{2}.\d-[A-Z]-[A-Z]{2}\d{2}\b',   #19 KRD-KRA-21.1-P-MX80
    '\b[A-Z]{3}-[A-Z]{4}-[A-Z]{3}\d{3}-[A-Z]{2}\d\b',   #19 STV-STAV-ATS286-ER1
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]{4}\d-[A-Z]{2}\d{3}\b',   #19 KRD-ANP-OPTS2-MX480
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]{2}-[A-Z]\d\-[A-Z]\d{4}\b',   #19 DAG-MHK-CR-P1-C7604
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]{3}\d{3}-[A-Z]{2}\d{2}\b',   #19 KRD-ANP-PSE212-MX80
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]{2}-[A-Z]{4}\d-[A-Z]\d\b',   #19 VLG-SER-CS-SVET5-R0
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]{3}\d{4}\b',   #19 LIM-KAM-ACX1000
    '\b[A-Z]{3}-[A-Z]{3}-\d{2}-[A-Z]\d-[A-Z]\d{4}\b',   #19 KRD-VSL-07-R4-C7206
    '\b\d{4}_\d{3}_[A-Z]{3}\d_[A-Z]{2}\d{2}[A-Z]\b',   #19 7609_244_ATS4_AR63A
    '\b[A-Z]{4}_[A-Z]{3}\d{3}_\d{2}-[A-Z]{3}\d\b',   #19 KLGA_ATS253_05-BPE1
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]{3}-[A-Z]{3}\d{4}\b',   #19 AST-LIM-KAM-ACX1000
    '\b\d{4}_[A-Z]{8}_[A-Z]{2}\d{2}[A-Z]\b',   #19 7609_KLIMOVSK_AR40A
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]{3}\d{2}-[A-Z]\d{4}\b',   #19 ING-NZR-ATS22-C7206
    '\b[A-Z]{3}-[A-Z]{3}-\d{2}-[A-Z]-[A-Z]{2}\d{3}\b',   #19 KRD-KRA-20-P-MX480
    '\b[A-Z]{3}-[A-Z]{3}-\d{2}.\d-[A-Z]-[A-Z]{2}\d{2}\b',   #19 KRD-KRA-68.1-P-MX80
    '\b[A-Z]{3}-[A-Z]{3}-\d{2}.\d-[A-Z]-[A-Z]{2}\d{3}\b',   #20 KRD-KRA-52.1-P-MX480
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]{2}\d{3}-[A-Z]-[A-Z]{2}\d{2}\b',   #20 KRD-SCH-AR321-R-MX80
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]{3}\d{2}-[A-Z]-[A-Z]{2}\d{2}\b',   #20 KRD-SCH-PSE50-R-MX80
    '\b[A-Z]{12}\d{3}[A-Z]{2}\d{3}\b',   #20 ROSHKTHKMRKS106MX480
    '\b[A-Z]{3}-[A-Z]{3}-\d{3}-[A-Z]\d-[A-Z]{2}\d{3}\b',   #20 KLM-ELS-004-R1-MX480
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]{3}\d-[A-Z]-[A-Z]{2}\d{3}\b',   #20 KRD-SCH-RGR3-P-MX480
    '\b\d{4}_[A-Z]{7}.[A-Z]{4}.[A-Z]{2}\b',   #20 7201_KASHIRA.ESMR.RU
    '\b\d{4}_\d{3}_[A-Z]{3}\d{2}_[A-Z]{2}\d{2}[A-Z]\b',   #20 7609_261_ATS15_AR62A
    '\b[A-Z]{3}-[A-Z]{4}-[A-Z]{3}\d{2}-[A-Z]{2}\d{4}\b',   #21 STV-STAV-ATS56-ER1555
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]{3}\d{3}-[A-Z]-[A-Z]{2}\d{2}\b',   #21 KRD-SCH-PSE464-P-MX80
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]{5}-[A-Z]{2}-[A-Z]{2}\d{2}\b',   #21 KRD-SCH-LAURA-AR-MX80
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]\d{6}-[A-Z]{2}\d{2}\b',   #21 ADG-JBL-R254074-MX48
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]{4}\d-[A-Z]\d-[A-Z]{2}\d{2}\b',   #21 KRD-APR-OPTS2-P1-MX80
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]-[A-Z]{2}\d{2}-[A-Z]{2}-\d-\d\b',   #21 KRD-ARM-P-MX80-PS-3-4
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]\d{6}-[A-Z]{2}\d{3}\b',   # 21 ADG-JBL-R254074-MX480
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]{4}-[A-Z]\d-[A-Z]{2}\d{3}\b',   #21 KRD-SCH-AMTS-P2-MX480
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]{3}\d{2}-[A-Z]-[A-Z]{2}\d{3}\b',   #21 KRD-SCH-PSE52-P-MX480
    '\b[A-Z]{3}-[A-Z]{3}-\d{3}-[A-Z]{3}-[A-Z]{4}\d\b',   #21 [A-Z]{3}-[A-Z]{3}-\d{3}-[A-Z]{3}-[A-Z]{4}\d
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]{2}-[A-Z]{3}\d-[A-Z]{2}\d{3}\b',   #21 KLM-ELS-CR-BPE1-MX960
    '\b[A-Z]{3}-[A-Z]{4}\d-[A-Z]{2}\d{2}[A-Z]-[A-Z]{3}\d{2}\b',   #21 SPB-EFIM4-NE40E-IXR01
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]{2}-[A-Z]{3}\d-[A-Z]\d{4}\b',   #21 DAG-MHK-CR-BPE1-C7206
    '\b[A-Z]{3}-[A-Z]{3}-\d{4}-[A-Z]{2}-[A-Z]\d{4}\b',   #21 KRD-GEL-5847-SR-N7250
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]{4}\d{2}-[A-Z]-[A-Z]{2}\d{3}\b',   #22  KRD-SCH-OPTS65-P-MX480
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]{3}\d{3}-[A-Z]-[A-Z]{2}\d{3}\b',   #22 KRD-SCH-PSE471-P-MX480
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]{4}-[A-Z]{2}\d-[A-Z]{2}\d{3}\b',   #22 KRD-ADG-MKOP-AR1-MX480
    '\b[A-Z]{3}-[A-Z]{4}-[A-Z]{3}\d-[A-Z]\d-[A-Z]\d{4}\b',   #22 STV-KOCH-ATS2-R1-C7206
    '\b[A-Z]{3}-[A-Z]{4}-[A-Z]{4}-[A-Z]\d-[A-Z]\d{4}\b',   #22 RST-ROST-RMTS-R1-C7206
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]{4}\d-[A-Z]\d-[A-Z]{2}\d{3}\b',   #22 KRD-GOR-OPTS4-P1-MX480
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]{2}-[A-Z]{4}\d-[A-Z]{4}\d\b',   #22 DAG-MHK-CR-BRAS9-SUNT4
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]{4}\d{2}-[A-Z]\d{5}[A-Z]\b',   #22 KRD-SCH-OPTS62-H12700E
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]{2}-[A-Z]{4}\d-[A-Z]\d{4}\b',   #22 DAG-MHK-CR-ASBR6-C2811
    '\b[A-Z]{3}-[A-Z]{3}-\d{2}-[A-Z]\d{6}-[A-Z]{2}\d{3}\b',   #24 ADG-MKP-53-R254005-MX480
    '\b[A-Z]{3}-[A-Z]{3}-[A-Z]{4}-[A-Z]{2}\d{3}-\d.\d{3}\b',   #24 KRD-KRA-ASBR-MX960-0.100
    '\bTULA-\w*-DR\b',   #TULA-ARKHANGELSKOYE-DR
    '\bRO\w*MX480\b',   #ROMLLSHLH33MX480
    '\bRO\w*MX80\b',
    '\bRO\w*MX480C\b',   #RORSTGZT49MX480C
    '\bRO\w*C3745\b'   #ROCLTKMRKS65C3745
    #'RO\w*\d[A-Z]'   #RORSTGZT49MX480C
]
listHostExcn = [   #список для исключений найденных по регулярным выражениям определенных значений. Проблема DATA-IX
    'DATA-IX'
]

serhHost(' M7-CR9-A ')