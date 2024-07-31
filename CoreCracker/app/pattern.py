patnHost = [    #список регулярных выражений для поиска HostName. Шаблоны располагаются по воссрастанию количества символов. Решение проблемы UAK6-CR4-B - M7-CR9-A
    '[A-Z]\d-[A-Z]{2}\d',   #6 M7-AR3
    '[A-Z]{3}-[A-Z]{2}\d',   #7 MRK-AR1
    '[A-Z]{4}-[A-Z]{2}',   #7 ALIC-AR
    '[A-Z]{3}-[A-Z]{2}\d',   #7 BMK-AR1
    '[A-Z]{3}\d-[A-Z]\d',   #7 UAK9-R1
    '[A-Z]{2}\d-[A-Z]{3}',   #7 HX0-GRZ
    '[A-Z]\d-[A-Z]{2}\d{2}',  #7 M7-AR10
    '[A-Z]\d-[A-Z]{3}\d',   #7 M7-ASW1
    '[A-Z]\d{2}-[A-Z]{2}\d',   #7 M10-AR2
    '[A-Z]\d-[A-Z]{2}\d-[A-Z]',  #8 M7-CR9-A
    '[A-Z]{4}-[A-Z]{2}\d',  #8 FRKT-CR5
    '[A-Z]{3}\d{2}-[A-Z]\d',   #8 UAK10-R1
    '[A-Z]\d{2}-[A-Z]{3}\d',   #8 M10-ASW3
    '[A-Z]{3}-[A-Z]{3}\d',   #8 IGN-CON1
    '[A-Z]{3}\d-[A-Z]{2}\d',   #8 UAK8-SR2
    '[A-Z]{3}\d-[A-Z]\d{2}',   #8 CXK6-A23
    '[A-Z]{3}\d-[A-Z]{3}',   #8 CXK6-PVL
    '[A-Z]\d-[A-Z]{4}\d',   #8 M7-ASTK1
    '[A-Z]\d-[A-Z]{3}\d{2}',   #8 M7-ASW10
    '[A-Z]\d{2}-[A-Z]{2}\d{2}',   #8 M10-AR10
    '[a-z]{3}-[a-z]{3}\d',   #8 ufa-rgr2
    '[a-z]{3}\d-[a-z]{2}\d',   #8 uak7-ar1
    '[A-Z]{4}-[A-Z]{3}\d',  #9 KLNG-RGR4
    '[A-Z]{3}\d-[A-Z]{3}\d',   #9 UAK6-CON3
    '[A-Z]{3}-[A-Z]{2}-[A-Z]\d',   #9 AST-CR-R1
    '[A-Z]{3}\d-[A-Z]{3}\d',   #9 UAK8-RGR1
    '[A-Z]{3}\d{2}-[A-Z]{2}\d',   #9 UAK10-SR2
    '[A-Z]{3}\d-[A-Z]{3}\d',   #9 UAK1-SSW6
    '[A-Z]{3}\d-[A-Z]{3}\d',   #9 UAK9-ASW1
    '[A-Z]{4}-[A-Z]{2}\d{2}',   #9 VLDK-SW12
    '[A-Z]{5}-[A-Z]{2}\d',   #9 BRVSK-AR1
    '[A-Z]{4}-[A-Z]{2}\d{2}',   #9 IVNV-AR23
    '[A-Z]{2}\d-[A-Z]{3}\d{2}', #9 HR0-ATS43
    '[A-Z]{3}\d-[A-Z]{4}',   #9 CXK6-NVOR
    '[A-Z]{4}-[A-Z]{2}\d{2}',   #9 MSCW-AR14
    '[A-Z]{3}\d-[A-Z]{2}-[A-Z]',   #9 UAK1-CR-A
    '[A-Z]{3}-[A-Z]{4}\d',   #9 GCU-SSTK1
    '[A-Z]{3}-[A-Z]{3}\d{2}',   #9 GCU-ASW14
    '[A-Z]\d{2}-[A-Z]{4}\d',   #9 M10-ASTK1
    '[A-Z]\d{2}-[A-Z]{3}\d{2}',   #9 M10-ASW10
    '[A-Z]\d{2}-[A-Z]{2}\d-[A-Z]',   #9 M10-CR7-B
    '\d{2}-[A-Z]{2}-[A-Z]{2}\d',   #9 51-PZ-AR1
    '[A-Z]{3}-\d-[A-Z]{3}',   #9 VPN-1-TLT
    '[a-z]{3}\d-[a-z]{3}\d',   #9 uak7-con1
    '[a-z]{4}-[a-z]{3}\d',   #9 kirv-bpe3
    '[a-z]{3}\d-[a-z]{2}-[a-z]',   #9 uak7-cr-a
    '[A-Z]{3}\d-[A-Z]{2}\d-[A-B]',  # 10 UAK6-CR4-B
    '[A-Z]{4}-[A-Z]{4}\d',   #10 IZHK-BRAS1
    '[A-Z]{4}-[A-Z]{3}\d{2}',   #10 NNOV-BPE21
    '[A-Z]{4}-[A-Z]{2}\d-[A-Z]',   #10 SPBR-CR4-A
    '\d{2}-[A-Z]{3}-[A-Z]{2}\d',   #10 23-NVP-AR1
    '[A-Z]{3}\d{2}-[A-Z]{3}\d',    #10 UAK10-ASW1
    '[A-Z]{3}-[A-Z]{3}-[A-Z]\d',   #10 KLM-YSK-R1
    '[A-Z]{3}\d-[A-Z]{4}\d',   #10 UAK5-SSTK1
    '[A-Z]{4}-[A-Z]{2}\d-\d',   #10 VLDK-SW5-2
    '[A-Z]{4}-[A-Z]{2}\d{3}',   #10 VLMR-DR001
    '[A-Z]{3}-[A-Z]\d-[A-Z]{2}\d',  #10 UFA-N2-AR1
    '[A-Z]{3}-\d{2}-[A-Z]{3}',   #10 VPN-10-TLT
    '[a-z]{4}-[a-z]{3}\d{2}',   #10 kirv-rgr11
    '[a-z]{4}-[a-z]{2}\d-[a-z]',   #10 smra-cr5-a
    '[A-Z]{4}\d{2}-[A-Z]{2}\d',   #10 YSLV21-DR1
    '[A-Z]\d-[A-Z]{3}-[A-Z]{2}\d',   #10 M7-DPC-SW1
    '[A-Z]\d{2}-[A-Z]{5}\d',   #10 M10-VTARA4
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{2}\d',   #11 MRK-LTC-AR1
    '[A-Z]{4}-[A-Z]{4}\d{2}',   #11 SRSK-BRAS11
    '\d{2}-[A-Z]{3}-[A-Z]{3}\d',   #11 13-ARD-CON1
    '\d{2}-[A-Z]{4}-[A-Z]{2}\d',   #11 11-EMVA-AR1
    '[A-Z]{3}\d{2}-[A-Z]{3}\d{2}',   #11 UAK10-ESR13
    '[A-Z]{3}-[A-Z]{2}-[A-Z]{3}\d',   #11 AST-CR-BPE1
    '[A-Z]{3}-[A-Z]{2}-[A-Z]{2}-\d',   #11 DGS-BB-MX-1
    '[A-Z]{4}-[A-Z]{3}-[A-Z]\d',   #11 NVSK-DPC-R1
    '[A-Z]{4}-[A-Z]{3}\d{3}',   #11 VLDK-ASW117
    '[A-Z]{4}-\d{2}-[A-Z]{2}\d',   #11 MCEN-39-AR1
    '[A-Z]{3}\d{2}-[A-Z]{2}\d-[A-Z]',   #11 UAK10-CR5-A
    '[A-Z]{3}\d-[A-Z]{5}\d',   #11 UAK1-VTARA
    '[A-Z]\d{2}-[A-Z]{3}-[A-Z]{2}\d',   #11 M10-DPC-SW1
    '[A-Z]{3}-[A-Z]\d{2}-[A-Z]{2}\d',   #11 UFA-N10-AR1
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{3}\d',   # 12 BLR-MZG-VGW2
    '[A-Z]{4}-[A-Z]{3}-[A-Z]{2}\d',   #12 DAVL-LTC-AR1
    '[A-Z]{3}-[A-Z]{4}-[A-Z]{2}\d',   #12 UFA-CORE-SR2
    '[A-Z]{3}-[A-Z]{3}\d-[A-Z]{2}\d',   #12 KVL-ATS2-AR1
    '[A-Z]\d{2}-[A-Z]{6}\d',   #11 [A-Z]\d{2}-[A-Z]{6}\d
    '[A-Z]\d{2}-[A-Z]{5}\d{2}',   #11 M10-VTARA10
    '\d{2}-[A-Z]{5}-[A-Z]{2}\d',   #12 35-USTUG-AR1
    '\d{2}-[A-Z]{4}-[A-Z]{3}\d',   #12 13-ATSH-CON1
    '[A-Z]{4}_\d{3}-[A-Z]{2}\d',    #12 ZHRD_355-DR1
    '[A-Z]{4}-[A-Z]{3}\d{4}',   #12 MSCW-ASW1012
    '[A-Z]{4}_[A-Z]\d{2}-[A-Z]{2}\d',   #12 SMLK_A27-DR1
    '[A-Z]\d{2}[A-Z]{5}-[A-Z]{2}\d',   #12 M10TMGUS-AR1
    '[A-Z]{3}-[A-Z]{3}-\d{2}[A-Z]\d',   #12 SVO-VLK-25P1
    '\d{1,2}-[A-Z]{4}\d-[A-Z]{2}\d',   #12 23-ARMV3-AR1
    '\d{2}-[A-Z]{3}\d{2}-[A-Z]{2}\d',   #12 15-ALA02-AR1
    '\d{2}-[A-Z]{4}-[A-Z]{2}\d{2}',   #12 05-MHKL-AR10
    '[a-z]{3}-[a-z]{4}-[a-z]{2}\d',   #12 bor-cats-ar1
    '[A-Z]{4}-[A-Z]{3}\d{2}-[A-Z]{2}',   #13 CHEB-ATS55-DR
    '[A-Z]{4}-[A-Z]{4}-[A-Z]{2}\d',   #13 PNZA-CORE-DR1
    '[A-Z]{4}-[A-Z]{3}\d-[A-Z]{2}\d',   #13 NOVK-ATS7-AR1
    '[A-Z]{4}-[A-Z]{3}-[A-Z]{3}\d',   #13 CHKM-LTC-VGW2
    '[A-Z]{3}-[A-Z]{4}-[A-Z]{2}\d{2}',   #13 UFA-CORE-AR11
    '[A-Z]{3}-[A-Z]{4}-[A-Z]{3}\d',   #13 UFA-CORE-BPE2
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{2}-[A-Z]\d',   #13 VLG-KTL-CS-R0
    '[A-Z]{3}-[A-Z]{3}-\d{2}-[A-Z]\d',   #13 SVO-CHI-03-P1
    '\d{2}-[A-Z]{3}-\d{2}-[A-Z]{2}\d',   #13 23-KRA-24-AR1
    '[A-Z]{3}-[A-Z]{3}-\d{2}-[A-Z]\d',   #13 SVO-ARD-03-P1
    '[A-Z]{3}-[A-Z]{2}-\d{3}-[A-Z]\d',   #13 AST-AS-025-R1
    '[A-Z]{3}-[A-Z]{2}-[A-Z]{3}-[A-Z]\d',  #13 AST-AS-BHT-R1
    '[A-Z]{3}-[A-Z]{3}-\d{2}-[A-Z]\d',   #13 SVO-BES-03-P1
    '\d{2}-[A-Z]{4}\d{2}-[A-Z]{2}\d',   #13 35-VLGD27-AR1
    '\d{2}-[A-Z]{4}\d-[A-Z]{3}\d',   #13 13-KVLA2-CON1
    '[A-Z]{4}_\d{4}-[A-Z]{2}\d',   #13 UVRV_5840-DR1
    '[A-Z]{4}-[A-Z]{3}-[A-Z]{2}\d{2}',   #13 EBRG-DPC-SW10
    '[A-Z]{4}-[A-Z]{2}\d{2}-[A-Z]{2}\d',   #13 ZLND-UD03-AR1
    '[A-Z]{4}-[A-Z]{3}-[A-Z]{2}\d',  #13 KRDL-LTC-AR1
    '[A-Z]{4}_\d{4}-[A-Z]{2}\d',   #13 ZNAM_5223-DR1
    '[A-Z]{4}-[A-Z]{3}-[A-Z]{2}\d{2}',   #13 EBRG-DPC-SW10
    '[A-Z]\d{2}[A-Z]{5}-[A-Z]{3}\d',   #13 M10TMGUS-ASW1
    '\d{2}-[A-Z]{3}\d{3}-[A-Z]{2}\d',   #13 23-KRD283-AR1
    '\d{2}-[A-Z]{5}-[A-Z]{3}\d',   #13 15-VLKCR-BPE2
    '[a-z]{2}\d-[a-z]{3}-[a-z]{3}\d{2}',   #13 pe2-lab-ats66
    '[a-z]{4}-[a-z]{3}-[a-z]{3}\d',   #13 yosh-gts-con1s
    '[a-z]{4}-[a-z]{4}-[a-z]{2}\d',   #13 nnov-nmts-cr9
    '[a-z]{4}-[a-z]{3}\d-[a-z]{2}\d',   #13 sarv-ats3-ar2
    '[a-z]{4}-[a-z]{4}-[a-z]{2}\d',   #13 nnov-nmts-cr7
    '[a-z]{3}-[a-z]{4}-[a-z]{3}\d',   #13 bor-cats-con1
    '[A-Z]{4}-[A-Z]{3}\d{2}-[A-Z]{2}\d',  #14 TLTT-ATS22-SR1
    '[A-Z]{4}-[A-Z]{4}-[A-Z]{3}\d',    #14 SMRA-AMTS-BPE1
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{4}\d{2}',   #14 BLB-LTC-BRAS17
    '[A-Z]{4}-[A-Z]{2}\d{3}-[A-Z]{2}\d',   #14 SZRN-PS901-AR1
    '[A-Z]{4}-[A-Z]{4}\d-[A-Z]{2}\d',   #14 SMRA-OPTS3-AR1
    '[A-Z]{3}-[A-Z]{2}-[A-Z]\d-[A-Z]{2}\d{2}',   #14 KCR-UD-R1-MX80
    '\d{2}-[A-Z]{4}\d{3}-[A-Z]{2}\d',   #14 78-SPBR343-DR1
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{3}-[A-Z]\d',   #14 VLG-SAH-KSL-R0
    '[A-Z]{3}-[A-Z]{3}-[A-Z]-[A-Z]{2}\d{2}',   #14 'KRD-KMK-P-MX48
    '[A-Z]{3}-[A-Z]{4}-\d{2}-[A-Z]\d',   #14 SVO-PAVL-01-P1
    '[A-Z]{3}-[A-Z]{3}-\d{3}-[A-Z]\d',   #14 KBR-NLK-096-R1
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{3}-[A-Z]\d',   #14 SVO-VLK-HOL-P1
    '[A-Z]{3}-[A-Z]{5}\d-[A-Z]{2}\d',   #14 UNI-OTMUS2-AR1
    '[A-Z]{4}-[A-Z]{3}\d{2}-[A-Z]{3}',   #14 CHEB-ATS55-BPE
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{2}-[A-Z]{2}\d',   #14 SVO-VLK-CR-RR2
    '[A-Z]{4}_[A-Z]{3}\d{2}-[A-Z]{2}\d',   #14 BLGD_ATS21-DR1
    '\d{4}_\d{3}_[A-Z]{2}\d{2}[A-Z]',   #14 7609_236_AR75A
    '[A-Z]{4}-[A-Z]{5}-[A-Z]{2}\d',   #14 RZAN-KRBLN-DR1
    '[A-Z]{4}_[A-Z]\d{2}-[A-Z]{4}\d',   #14 LPTZ_A22-ASBR1
    '[A-Z]{4}_[A-Z]{3}-[A-Z]{4}\d',   #14 LPTZ_MTS-BRAS1
    '[A-Z]{4}-[A-Z]{2}\d-[A-Z]{2}\d{3}',   #14 CHRK-AR1-MX480
    '[A-Z]{3}-[A-Z]{2}-[A-Z]{4}-[A-Z]\d',   #14 AST-CR-IPOE-R1
    '[A-Z]{4}-[A-Z]{3}-[A-Z]{3}\d{2}',   #14 NVSK-DPC-SSW11
    '[A-Z]{4}_\d{3}-\d-[A-Z]{2}\d',   #14 TMBV_247-2-DR1
    '[A-Z]{4}-[A-Z]{3}-[A-Z]{4}\d',   #14 EBRG-DPC-ASTK1
    '[A-Z]{3}-[A-Z]{3}\d{2}-[A-Z]{2}\d{2}',   #14 KRD-NVR61-MX80
    '\d{2}-[A-Z]{6}\d-[A-Z]{2}\d',   #14 23-SOHIRF1-AR2
    '\d{2}-[A-Z]{4}\d{2}-[A-Z]{3}\d',   #14 30-ASTR51-BPE1
    '[a-z]{4}-[a-z]{3}\d-[a-z]{3}\d',   #14 kstv-ats3-con1
    '[a-z]{4}-[a-z]{3}\d{2}-[a-z]{2}\d',   #14 dzer-ats21-ar1
    '[a-z]{4}-[a-z]{4}-[a-z]{3}\d',   #14 skls-cats-con1
    '[A-Z]{4}-[A-Z]{6}-[A-Z]{2}\d',     #15 VLZS-BEREZA-AR1
    '[A-Z]{3}-[A-Z]{4}-[A-Z]{4}\d{2}',   #15 UFA-CORE-BRAS21
    '[A-Z]{3}-[A-Z]{4}-[A-Z]{3}\d-[A-Z]',   #15 UFA-CORE-VGW3-R
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{4}-[A-Z]\d',   #15 VLG-VOL-MGOR-R0
    '[A-Z]{3}-[A-Z]{3}-[A-Z]-[A-Z]{2}\d{3}',  # 15 KRD-KOR-P-MX480
    '[A-Z]{3}-[A-Z]{3}-[A-Z]\d-[A-Z]{2}\d{2}',  # 15 KCR-ADH-R1-MX80
    '[A-Z]{3}-[A-Z]{3}-[A-Z]-[A-Z]{2}\d{3}',  # 15 KRD-ARM-P-MX480
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{3}\d-[A-Z]\d',  # 15 VLG-VOL-BAT3-R0
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{2}\d{2}-[A-Z]\d',   #15 VLG-KAL-PS35-R0
    '[A-Z]{4}-[A-Z]{5}\d-[A-Z]{2}\d',   #15 ARBZ-OTMUS2-AR1
    '[A-Z]{4}-[A-Z]{3}\d{3}-[A-Z]{2}\d',   #15 KIRV-PSC408-AR1
    '[A-Z]{4}-[A-Z]{5}\d-[A-Z]{2}\d',   #15 SUNA-OTMUS3-AR2
    '[A-Z]{2}\d{2}-\d[A-Z]{2}\d{2}-[A-Z]{4}',   #15 MX80-1AG45-BALT
    '[A-Z]{3}-[A-Z]{3}-\d{3}-[A-Z]{2}\d',   #15 'KBR-NLK-040-AS1'
    '[A-Z]{4}-[A-Z]{3}\d{2}-[A-Z]{3}\d',   #15 KIRV-ATS65-BPE1
    '[A-Z]{2}\d{3}-[A-Z]{4}-[A-Z]{4}',   #15 MX104-CATS-KRES
    '[A-Z]{2}\d{3}-\d[A-Z]{2}\d{3}-[A-Z]{2}',   #15 MX104-1AG327-PZ
    '[A-Z]{4}_[A-Z]{3}\d{3}-[A-Z]{2}\d',   #15 KLGA_ATS253-DR1
    '[A-Z]{5}_[A-Z]{3}\d{2}-[A-Z]{2}\d',   #15 GUBKN_ATS40-DR1
    '[A-Z]{4}-[A-Z]{2}\d{2}-[A-Z]{3}\d{2}',   #15 BRAS-ME60-ATS35
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{3}-[A-Z]{2}\d',   #15 KLM-KMS-ART-MX1
    '[A-Z]{5}-[A-Z]{3}\d{2}-[A-Z]{2}\d',   #15 STOSK-ATS44-DR1
    '\d{2}-[A-Z]{4}-[A-Z]{2}\d-[a-z]{2}\d',   #15 29-SVDV-DR1-re0
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{2}-[A-Z]{3}\d',   #15 SVO-VLK-CR-BPE1
    '[A-Z]{4}-[A-Z]{2}\d{3}[A-Z]-[A-Z]{2}\d',   #15 KAZN-PS510B-AR1
    '[A-Z]{4}-[A-Z]{2}\d{4}-[A-Z]{2}\d',   #15 KAZN-PS5122-AR1
    '[A-Z]{4}-[A-Z]{2}\d-\d{2}-[A-Z]{2}\d',   #15 NCHL-PS2-02-AR1
    '[A-Z]{4}_[A-Z]{6}-[A-Z]{2}\d',   #15 BLGD_ATSDUB-DR1
    '[A-Z]{3}-[A-Z]{3}-\d{2}-[A-Z]{3}\d',   #15 SVO-ALA-02-CON1
    '[A-Z]{5}_\d{3}-1-[A-Z]{2}\d',   #15 STRTL_271-1-DR1
    '[A-Z]{3}-[A-Z]{3}-\d{2}-[A-Z]{3}\d',   #15 SVO-OCT-02-CON1
    '[A-Z]{4}-[A-Z]{3}\d{2}-\d{4}',   #15 CHEB-ATS62-7200
    '\d{1,2}-[A-Z]{8}-[A-Z]{2}\d{1,2}',   #15 23-SOHIAMTS-AR1
    '\d{2}-[A-Z]{5}\d{3}-[A-Z]{2}\d',   #15 23-SOHIR131-AR1
    '\d{2}-[A-Z]{4}\d{4}-[A-Z]{2}\d',   #15 34-VGRD0472-AR1
    '\d{2}-[A-Z]{6}-[A-Z]{2}\d',  # 15 15-VLKSPU-AR1
    '\d{2}-[A-Z]{4}\d{3}-[A-Z]{3}\d',  # 15 07-NCHK040-BPE3
    '\d{2}-[A-Z]{6}\d{2}-[A-Z]{2}\d',   #15 61-SHAKHT23-AR1
    '[a-z]{4}-[a-z]{3}\d{3}-[a-z]{2}\d',   #15 nnov-ats342-ar1
    '[a-z]{4}-[a-z]{2}\d{4}-[a-z]{2}\d',   #15 nnov-ps2251-ar1
    '[a-z]{4}-[a-z]{3}\d{2}-[a-z]{3}\d',   #15 dzer-ats25-con1
    '[A-Z]{3}-[A-Z]{4}-[A-Z]{2}\d-[A-Z]{2}\d',  #16 STV-NEVN-PS0-ER1
    '[A-Z]{3}-[A-Z]{4}-[A-Z]\d-[A-Z]{2}\d{2}',  #16 KCR-UCHK-R1-MX80
    '[A-Z]{4}-[A-Z]{3}\d-\d{2}-[A-Z]{2}\d',   #16 ORNB-PSE4-16-AR1
    '[A-Z]{2}\d{2}-\d[A-Z]{2}\d{3}-[A-Z]{4}',   #16 MX80-1AG563-ZAOZ
    '[A-Z]{3}-[A-Z]{3}-\d{2}[A-Z]{3}-[A-Z]\d',   #16 VLG-VOL-25LET-R0
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{3}\d{2}-[A-Z]\d',   #16 VLG-VOL-RKR37-R0
    '[A-Z]{2}\d{2}-\d[A-Z]{2}\d{3}-[A-Z]{4}',   #16 MX80-1AG557-APAT
    '[a-z]{4}-[a-z]{3}\d{2}-[a-z]{4}\d',  #16 pnza-ats52-sorm1
    '[A-Z]{2}\d{3}-\d[A-Z]{2}\d{2}-[A-Z]{4}',   #16 MX104-1AG56-BGRT
    '[A-Z]{2}\d{2}-\d[A-Z]{2}\d{2}-[A-Z]{5}',   #16 MX80-1AG39-LOUHI
    '[A-Z]{2}\d{3}-\d[A-Z]{2}\d{2}-[A-Z]{4}',   #16 MX104-1AG30-SORT
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{2}-[A-Z]{4}\d',   #16 KBR-NLK-CR-BRAS2
    '[A-Z]{4}-[A-Z]{3}\d{2}-[A-Z]{3}\d{2}',   #16 SRTV-ATS73-BPE11
    '[A-Z]{4}-[A-Z]{5}-[A-Z]{4}\d',   #16 TLTT-TOTEL-BRAS1
    '[A-Z]{2}\d{3}-\d[A-Z]{2}\d{3}-[A-Z]{3}',   #16 MX480-1AG210-SPB
    '[A-Z]{2}\d{3}-\d[A-Z]{5}-[A-Z]{3}',   #16 MX480-1AGMMT-SPB
    '[A-Z]{2}\d{3}-\d[A-Z]{2}\d{3}-[A-Z]{3}',   #16 MX960-1AG210-SPB
    '[A-Z]{2}\d{3}-\d[A-Z]{5}-[A-Z]{3}',   #16 MX960-1AGMMT-SPB
    '[A-Z]{3}-[A-Z]{3}-[A-Z]\d-[A-Z]\d{4}',   #16 DAG-BNK-R1-C7206
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{2}-[A-Z]\d{4}',   #16 DAG-MHK-CR-C2851
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{5}-[A-Z]\d',   #16 VLG-PAL-PUTIL-R0
    '[A-Z]{3}-[A-Z]{3}-[A-Z]\d-[A-Z]\d{4}',   #16 DAG-VCH-R1-C2811
    '[A-Z]{3}-[A-Z]{3}-[A-Z]\d-[A-Z]\d{4}',   #16 DAG-TLT-R1-C2811
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{5}-[A-Z]\d',   #16 VLG-KUM-BGORC-R0
    '[A-Z]{3}\d-[A-Z]{3}.[A-Z]{3}.[A-Z]{3}',   #16 CAR1-GRZ.NET.LOC
    '[A-Z]{4}-[A-Z]{2}\d{2}[A-Z]{3}-[A-Z]{2}\d',   #16 ULSK-LT95SRV-AR1
    '[A-Z]{4}-[A-Z]{4}\d{2}-[A-Z]{4}',    #16 TULA-OPTS27-ASBR
    '[A-Z]{4}-[A-Z]{2}\d{2}-\d{2}-[A-Z]{2}\d',   #16 NCHL-PS18-08-AR1
    '[A-Z]{3}\d{3}-[A-Z]{2}\d{3}[A-Z]\d-\d',   #16 TMB073-CX600X1-1
    '\d{1,2}-[A-Z]{7}-[A-Z]{2}\d{1,2}',   #16 23-KRDAMTS-DR2
    '[A-Z]{3}-[A-Z]{4}-[A-Z]{3}\d-[A-Z]{2}\d',   #17 STV-KISL-ATS5-ER1
    '[A-Z]{4}-[A-Z]{4}\d{3}-[A-Z]{2}\d',   #16 KAZN-OPTS512-AR1
    '[A-Z]{3}-[A-Z]{3}-\d.\d-[A-Z]{2}\d{2}',   #16 KRD-ANP-2.1-MX80
    '\d{2}-[A-Z]{8}-[A-Z]{3}\d',   #16 23-KRDRAMTS-BPE1
    '\d{2}-[A-Z]{9}-[A-Z]{2}\d',   #16 23-SOHILAURA-AR1
    '\d{2}-[A-Z]{9}-[A-Z]{2}\d',   #16 61-RNDNSUVOR-AR1
    '[A-Z]{4}\d{5}-[A-Z]{2}\d{2}-\d',   #16 SSNV79610-MX80-1
    '\d{2}-[A-Z]{3}-[A-Z]{2}\d-NOKIA',   #16 23-KUR-AR1-NOKIA
    '[a-z]{4}-[a-z]{3}\d{3}[a-z]{2}-[a-z]{2}\d',   #17 nnov-ats225bg-ar2
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{3}\d{3}-[A-Z]\d',   #17 VLG-VOL-KIR120-R0
    '[A-Z]{3}-[A-Z]{3}\d{2}-[A-Z]\d-[A-Z]{2}\d{2}',   #17 KCR-ATS25-R1-MX80
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{4}-[A-Z]-[A-Z]\d',   #17 VLG-GOR-KTLB-B-R0
    '[A-Z]{2}\d{2}-\d[A-Z]{2}\d{4}-[A-Z]{4}',   #17 MX80-1AG6620-BKST
    '[A-Z]{4}-[A-Z]{2}\d{2}[A-Z]\d{2}-[A-Z]{3}\d',   #17 ULSK-LT95S12-BPE4
    '[A-Z]{4}-[A-Z]{2}\d{2}[A-Z]{3}-[A-Z]{3}\d',   #17 ULSK-LT95SRV-BPE3
    '[A-Z]{2}\d{3}-\d[A-Z]{2}\d{3}-[A-Z]{4}',   #17 MX104-1AG440-BRVC
    '[A-Z]{3}-[A-Z]{3}-\d{2}-[A-Z]-[A-Z]{2}\d{2}',   #17 KRD-KRA-27-P-MX80
    '[A-Z]{3}-[A-Z]{3}-\d{2}.\d-[A-Z]{2}\d{2}',   #17 KRD-NVR-22.3-MX80
    '[A-Z]{3}-[A-Z]{3}-[A-Z]\d-[A-Z]\d{5}',   #17 DAG-DRB-R1-H12700
    '\d{2}-[A-Z]{4}-[A-Z]{2}\d-NOKIA',   #17 01-GIAG-AR1-NOKIA
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{3}-[A-Z]{4}\d',   #17 TVG-SVO-KIR-BRAS1
    '[a-z]{4}-[a-z]{5}\d{2}-[a-z]{3}\d',   #17 yosh-krasn76-con1
    '[A-Z]{3}-[A-Z]{4}-[A-Z]{3}\d{2}-[A-Z]{2}\d',   #18 STV-PTGR-ATS32-ER1
    '[A-Z]{3}-[A-Z]{3}-\d{3}-[A-Z]-[A-Z]{2}\d{2}',   #18 KRD-USP-001-P-MX80
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{3}-[A-Z]-[A-Z]{2}\d{2}',  #18 KRD-KRA-KPN-P-MX80
    '[A-Z]{3}-[A-Z]{3}-\d{2}-[A-Z]-[A-Z]{2}\d{3}',   #18 KRD-KRA-37-P-MX480
    '[A-Z]{3}-[A-Z]{3}-[A-Z]\d-[A-Z]\d-[A-Z]{2}\d{2}',   #18 KRD-SCH-F1-R1-MX80
    '[A-Z]{3}-[A-Z]{3}\d{2}-[A-Z]\d-[A-Z]{2}\d{3}',   #18 KCR-ATS20-R1-MX480
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{3}-[A-Z]{2}\d{2}-[A-Z]',   #18 KRD-OLG-ORB-MX80-P
    '[A-Z]{3}-[A-Z]{3}-\d{2}-[A-Z]\d-[A-Z]{2}\d{2}',   #18 KRD-LEN-07-R1-MX80
    '[A-Z]{4}-[A-Z]{9}-[A-Z]{2}\d',   #18 ZVEN-SHELANGER-AR1
    '[A-Z]{2}\d{3}-\d[A-Z]{2}\d{4}-[A-Z]{4}',   #18 MX104-1AG5056-KRZM
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{3}\d{2}-[A-Z]{2}\d{2}',   #18 ING-NZR-ATS22-MX80
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{2}-[A-Z]{3}\d{4}',   #18 AST-LIM-CS-ACX2100
    '[A-Z]{3}\d[A-Z]-\d-[A-Z]\d{2}.[A-Z]{3}.[A-Z]{2}',   #18 ASR1K-1-A52.VSI.RU
    '[A-Z]\d{4}-\d-[A-Z]\d{2}.[A-Z]{3}.[A-Z]{2}',   #18 C7301-1-A52.VSI.RU
    '[A-Z]{4}_[A-Z]{3}\d{3}_\d{2}-[A-Z]{2}\d',   #18 KLGA_ATS253_04-AR1
    '[A-Z]{2}\d{2}-\d[A-Z]{2}\d{5}-[A-Z]{4}',   #18 MX80-1AG79610-SSNV
    '[A-Z]{4}-[A-Z]{4}\d.[A-Z]{3}.[A-Z]{3}',   #18 KSTR-BRAS4.MSS.KOS
    '[A-Z]{3}\d-[A-Z]{3}\d{2}.[A-Z]{3}.[A-Z]{3}',   #18 ASR1-ATS22.NET.LOC
    '\d{2}-[A-Z]{3}\d{2}-[A-Z]{2}\d-NOKIA',   #18 23-NVR61-AR1-NOKIA
    '[A-Z]{3}-[A-Z]{3}-\d{2}.\d-[A-Z]-[A-Z]{2}\d{2}',   #19 KRD-KRA-21.1-P-MX80
    '[A-Z]{3}-[A-Z]{4}-[A-Z]{3}\d{3}-[A-Z]{2}\d',   #19 STV-STAV-ATS286-ER1
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{4}\d-[A-Z]{2}\d{3}',   #19 KRD-ANP-OPTS2-MX480
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{2}-[A-Z]\d\-[A-Z]\d{4}',   #19 DAG-MHK-CR-P1-C7604
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{3}\d{3}-[A-Z]{2}\d{2}',   #19 KRD-ANP-PSE212-MX80
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{2}-[A-Z]{4}\d-[A-Z]\d',   #19 VLG-SER-CS-SVET5-R0
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{3}\d{4}',   #19 LIM-KAM-ACX1000
    '[A-Z]{3}-[A-Z]{3}-\d{2}-[A-Z]\d-[A-Z]\d{4}',   #19 KRD-VSL-07-R4-C7206
    '\d{4}_\d{3}_[A-Z]{3}\d_[A-Z]{2}\d{2}[A-Z]',   #19 7609_244_ATS4_AR63A
    '[A-Z]{4}_[A-Z]{3}\d{3}_\d{2}-[A-Z]{3}\d',   #19 KLGA_ATS253_05-BPE1
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{3}-[A-Z]{3}\d{4}',   #19 AST-LIM-KAM-ACX1000
    '\d{4}_[A-Z]{8}_[A-Z]{2}\d{2}[A-Z]',   #19 7609_KLIMOVSK_AR40A
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{3}\d{2}-[A-Z]\d{4}',   #19 ING-NZR-ATS22-C7206
    '[A-Z]{3}-[A-Z]{3}-\d{2}-[A-Z]-[A-Z]{2}\d{3}',   #19 KRD-KRA-20-P-MX480
    '[A-Z]{3}-[A-Z]{3}-\d{2}.\d-[A-Z]-[A-Z]{2}\d{2}',   #19 KRD-KRA-68.1-P-MX80
    '\d{1,2}-[A-Z]{3}-\d{1,2}-[A-Z]{2}\d-NOKIA',   #19 23-KRA-37-AR1-NOKIA
    '[A-Z]{3}-[A-Z]{3}-\d{2}-[A-Z]\d-[A-Z]{2}\d{3}',   #19 KRD-KRA-61-P1-MX480
    '\d{2}-[A-Z]{4}\d{2}-[A-Z]{2}\d-NOKIA',   #19 01-MKOP53-AR1-NOKIA
    '[A-Z]{3}-[A-Z]{3}-\d{2}.\d-[A-Z]-[A-Z]{2}\d{3}',   #20 KRD-KRA-52.1-P-MX480
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{2}\d{3}-[A-Z]-[A-Z]{2}\d{2}',   #20 KRD-SCH-AR321-R-MX80
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{3}\d{2}-[A-Z]-[A-Z]{2}\d{2}',   #20 KRD-SCH-PSE50-R-MX80
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{3}-[A-Z]\d-[A-Z]{2}\d{2}',   #19 KRD-SCH-GMC-R2-MX80
    '\d{2}-[A-Z]{3}\d{3}-[A-Z]{2}\d-NOKIA',   #19 23-SCH131-AR1-NOKIA
    '[A-Z]{12}\d{3}[A-Z]{2}\d{3}',   #20 ROSHKTHKMRKS106MX480
    '[A-Z]{3}-[A-Z]{3}-\d{3}-[A-Z]\d-[A-Z]{2}\d{3}',   #20 KLM-ELS-004-R1-MX480
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{3}\d-[A-Z]-[A-Z]{2}\d{3}',   #20 KRD-SCH-RGR3-P-MX480
    '\d{4}_[A-Z]{7}.[A-Z]{4}.[A-Z]{2}',   #20 7201_KASHIRA.ESMR.RU
    '\d{4}_\d{3}_[A-Z]{3}\d{2}_[A-Z]{2}\d{2}[A-Z]',   #20 7609_261_ATS15_AR62A
    '\d{2}-[A-Z]{3}-[A-Z]\d{2}-[A-Z]{2}\d-NOKIA',   #20 23-ABN-R18-AR1-NOKIA
    '\d{2}-[A-Z]{3}\d{3}[A-Z]-[A-Z]{2}\d-NOKIA',   #20 23-SCH151R-AR1-NOKIA
    '\d{2}-[A-Z]{3}-\d.\d-[A-Z]{2}\d-NOKIA',   #20 23-ANP-2.1-AR1-NOKIA
    '\d{2}-[A-Z]{3}-[A-Z]{3}-[A-Z]{2}\d-NOKIA',  #20 23-OLG-ORB-AR1-NOKIA
    '[A-Z]{3}-[A-Z]{4}-[A-Z]{3}\d{2}-[A-Z]{2}\d{4}',   #21 STV-STAV-ATS56-ER1555
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{3}\d{3}-[A-Z]-[A-Z]{2}\d{2}',   #21 KRD-SCH-PSE464-P-MX80
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{5}-[A-Z]{2}-[A-Z]{2}\d{2}',   #21 KRD-SCH-LAURA-AR-MX80
    '[A-Z]{3}-[A-Z]{3}-[A-Z]\d{6}-[A-Z]{2}\d{2}',   #21 ADG-JBL-R254074-MX48
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{4}\d-[A-Z]\d-[A-Z]{2}\d{2}',   #21 KRD-APR-OPTS2-P1-MX80
    '[A-Z]{3}-[A-Z]{3}-[A-Z]-[A-Z]{2}\d{2}-[A-Z]{2}-\d-\d',   #21 KRD-ARM-P-MX80-PS-3-4
    '[A-Z]{3}-[A-Z]{3}-[A-Z]\d{6}-[A-Z]{2}\d{3}',   # 21 ADG-JBL-R254074-MX480
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{4}-[A-Z]\d-[A-Z]{2}\d{3}',   #21 KRD-SCH-AMTS-P2-MX480
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{3}\d{2}-[A-Z]-[A-Z]{2}\d{3}',   #21 KRD-SCH-PSE52-P-MX480
    '[A-Z]{3}-[A-Z]{3}-\d{3}-[A-Z]{3}-[A-Z]{4}\d',   #21 [A-Z]{3}-[A-Z]{3}-\d{3}-[A-Z]{3}-[A-Z]{4}\d
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{2}-[A-Z]{3}\d-[A-Z]{2}\d{3}',   #21 KLM-ELS-CR-BPE1-MX960
    '[A-Z]{3}-[A-Z]{4}\d-[A-Z]{2}\d{2}[A-Z]-[A-Z]{3}\d{2}',   #21 SPB-EFIM4-NE40E-IXR01
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{2}-[A-Z]{3}\d-[A-Z]\d{4}',   #21 DAG-MHK-CR-BPE1-C7206
    '[A-Z]{3}-[A-Z]{3}-\d{4}-[A-Z]{2}-[A-Z]\d{4}',   #21 KRD-GEL-5847-SR-N7250
    '\d{2}-[A-Z]{3}-\d{2}.\d-[A-Z]{2}\d-NOKIA',   #21 23-KRA-34.2-AR1-NOKIA
    '\d{2}-[A-Z]{3}-[A-Z]{3}\d-[A-Z]{2}\d-NOKIA', #21 23-SCH-RGR3-AR1-NOKIA
    '\d{2}-[A-Z]{3}-[A-Z]{4}-[A-Z]{2}\d-NOKIA',
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{4}\d{2}-[A-Z]-[A-Z]{2}\d{3}',   #22  KRD-SCH-OPTS65-P-MX480
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{3}\d{3}-[A-Z]-[A-Z]{2}\d{3}',   #22 KRD-SCH-PSE471-P-MX480
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{4}-[A-Z]{2}\d-[A-Z]{2}\d{3}',   #22 KRD-ADG-MKOP-AR1-MX480
    '[A-Z]{3}-[A-Z]{4}-[A-Z]{3}\d-[A-Z]\d-[A-Z]\d{4}',   #22 STV-KOCH-ATS2-R1-C7206
    '[A-Z]{3}-[A-Z]{4}-[A-Z]{4}-[A-Z]\d-[A-Z]\d{4}',   #22 RST-ROST-RMTS-R1-C7206
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{4}\d-[A-Z]\d-[A-Z]{2}\d{3}',   #22 KRD-GOR-OPTS4-P1-MX480
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{2}-[A-Z]{4}\d-[A-Z]{4}\d',   #22 DAG-MHK-CR-BRAS9-SUNT4
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{4}\d{2}-[A-Z]\d{5}[A-Z]',   #22 KRD-SCH-OPTS62-H12700E
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{2}-[A-Z]{4}\d-[A-Z]\d{4}',   #22 DAG-MHK-CR-ASBR6-C2811
    '[A-Z]{3}-[A-Z]{3}-[A-Z]-[A-Z]{2}\d{2}-[A-Z]{7}',   #22 KRD-GEL-P-MX80-YUZHNIY
    '\d{2}-[A-Z]{3}-[A-Z]{4}\d-[A-Z]{2}\d-NOKIA',   #22 23-APR-OPTS2-AR1-NOKIA
    '\d{2}-[A-Z]{3}-[A-Z]{3}\d{2}-[A-Z]{2}\d-NOKIA',   #22 23-SCH-PSE61-AR1-NOKIA
    '\d{2}-[A-Z]{3}-[A-Z]{2}\d{3}-[A-Z]{2}\d-NOKIA',   #22 23-SCH-AR581-AR1-NOKIA
    '\d{2}-[A-Z]{3}-[A-Z]\d-[A-Z]\d-[A-Z]{2}\d-NOKIA',   #22 23-SCH-F1-R1-AR1-NOKIA
    '\d{2}-[A-Z]{3}-[A-Z]{3}-[A-Z]\d-[A-Z]{2}\d-NOKIA',   #23 23-SCH-GMC-R2-AR1-NOKIA
    '[A-Z]{3}-[A-Z]{4}-[A-Z]{3}\d-[A-Z]{2}\d-[A-Z]\d{4}',   #23 STV-IPAT-ATS5-PE1-C7206
    '\d{2}-[A-Z]{3}-[A-Z]{2}-\d-\d-[A-Z]{2}\d-NOKIA',   #23 23-ARM-PS-3-4-AR1-NOKIA
    '\d{2}-[A-Z]{3}-[A-Z]{3}\d{3}-[A-Z]{2}\d-NOKIA',   #23 23-SCH-PSE471-AR1-NOKIA
    '\d{2}-[A-Z]{3}-[A-Z]{4}\d{2}-[A-Z]{2}\d-NOKIA',   #23 23-SCH-OPTS65-AR1-NOKIA
    '\d{2}-[A-Z]{3}-[A-Z]{3}-\d{2}-[A-Z]{2}\d-NOKIA',   #23 23-SCH-AVK-21-AR1-NOKIA
    '[A-Z]{3}-[A-Z]{3}-\d{2}-[A-Z]\d{6}-[A-Z]{2}\d{3}',   #24 ADG-MKP-53-R254005-MX480
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{4}-[A-Z]{2}\d{3}-\d.\d{3}',   #24 KRD-KRA-ASBR-MX960-0.100
    '[A-Z]{3}-[A-Z]{4}-[A-Z]{3}\d{2}-[A-Z]{2}\d-[A-Z]\d{4}',   #24 STV-STAV-ATS35-PE1-C7206
    '\d{2}-[A-Z]{3}-[A-Z]\d{6}-[A-Z]{2}\d-NOKIA',   #24 01-KRG-R254069-AR1-NOKIA
    '\d{2}-[A-Z]{3}-[A-Z]{7}-[A-Z]{2}\d-NOKIA',   #24 23-GEL-YUZHNIY-AR1-NOKIA
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{3}-[A-Z]{4}\d.[a-z]{3}.[a-z]{3}',   #25 TVG-SVO-VES-BRAS1.bng.ves
    '\d{2}-[A-Z]{3}-\d{2}.\d-\d{3}-[A-Z]{2}\d-NOKIA',   #25 23-KRA-52.5-115-AR1-NOKIA
    '\d{2}-[A-Z]{3}-[A-Z]{2}\d{3}-\d{2}-[A-Z]{2}\d-NOKIA',   #25 23-SCH-AR161-31-AR1-NOKIA
    '\d{2}-[A-Z]{3}-[A-Z]{5}-[A-Z]{2}-[A-Z]{2}\d-NOKIA',   #25 23-SCH-LAURA-AR-AR1-NOKIA
    '\d{2}-[A-Z]{3}-\d{2}.\d-[A-Z]{3}-[A-Z]{2}\d-NOKIA',   #25 23-NVR-61.4-POP-AR1-NOKIA
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{3}-[A-Z]{3}\d.[a-z]{3}\d[a-z].[a-z]{3}',   #26 TVG-SVO-VES-ASW1.asr9k.ves
    '\d{2}-[A-Z]{3}-[A-Z]{3}\d{3}-\d{2}-[A-Z]{2}\d-NOKIA',   #26 23-SCH-PSE439-61-AR1-NOKIA
    '[A-Z]{3}-[A-Z]{3}-[A-Z]{3}-[A-Z]{2}\d.[a-z]{3}\d{4}.[a-z]{3}',   #27 TVG-SVO-KIR-DR1.asr9006.kir
    '[A-Z]{3}-[A-Z]{4}-[A-Z]{3}\d{2}[A-Z]\d[A-Z]\d-[A-Z]{2}\d-[A-Z]\d{4}',   #28 STV-STAV-ATS24R4A2-PE1-C7206
    '\d{2}-[A-Z]{3}-[A-Z]{2}\d{3}-[A-Z]{3}\d{3}-[A-Z]{2}\d-NOKIA',   #29 23-SCH-AR142-PSE628-AR1-NOKIA
    'TULA-\w*-DR',   #TULA-ARKHANGELSKOYE-DR
    'RO\w*MX480',   #ROMLLSHLH33MX480
    'RO\w*MX80',
    'RO\w*MX480C',   #RORSTGZT49MX480C
    'RO\w*C3745'   #ROCLTKMRKS65C3745
    #'RO\w*\d[A-Z]'   #RORSTGZT49MX480C
]
listHostExcn = [   #список для исключений найденных по регулярным выражениям определенных значений. Проблема DATA-IX
    'DATA-IX'
]

patnIntc = [
    '(?:ge|xe|et)(-\d{1,2}/\d{1,2}/\d{1,2})', #JUN xe-1/33/22 #ge-1/33/22
    #'ge-\d{1,2}/\d{1,2}/\d{1,2}',
    #'xe-\d{1,2}/\d{1,2}/\d{1,2}',
    #'et-\d{1,2}/\d{1,2}/\d{1,2}',
    'GigabitEthernet\d{1,2}/\d{1,2}/\d{1,2}',   #HUA GigabitEthernet11/1/8
    '100GE\d{1,2}/\d{1,2}/\d{1,2}',   #HUA 100GE9/0/7
    '10GE\d{1,2}/\d{1,2}/\d{1,2}',   #HUA 100GE9/0/7'
    'Gi\d{1,2}/\d{1,2}',   #Cisco Gi1/1
    'Gi\d{1,2}/\d{1,2}/\d{1,2}:\d',     #Cisco 'Gi\d/\d{1,2}/\d{1,2}:\d'
    '\d{1,2}/\d{1,2}/[Cc]\d{1,2}/\d{1,2}',    #Nokia 2/1/c34/1
    'GE\d{1,2}/\d{1,2}/\d{1,2}:\d{1,2}',   #GE7/0/9:1
    'GE\d{1,2}/\d{1,2}/\d{1,2}',   #GE-7/0/9:1
    '\d{1,2}/\d{1,2}/c\d{1,2}',  # NokiA 1/6/c7
    '\d{1,2}/\d{1,2}/\d{1,2}'  #NOKIA 1/1/1
]

patnIntcAggn = {
    'Interface ae\d{1,2}',  #ae45
    'Interface Eth-Trunk\d{1,2}', #Eth-Trunk45
    'Interface lag-\d{1,2}',   #lag-
    'Interface as',
    '-mpls'
}

patnDictZabxDirn = {
    'host_A_B': str,
    'host_B_A': str,
    'host_A': str,
    'host_B': str,
    'IP_A': str,
    'IP_B': str,
    'strm': str,
    'highSpedFull': 0,
    'highSpedUp': 0,
    'highSpedDown': 0,
    'bitsRecd': 0,
    'bitsSent': 0,
    'tredBitsRecdMax': 0,
    'tredBitsSentMax': 0,
    'tredBitsRecdMaxAvrg': 0,
    'tredBitsSentMaxAvrg': 0,
    'tredListClokDegnRecd': list(),
    'tredListClokDegnSent': list(),
    'tredListClokLoadRecd': list(),
    'tredListClokLoadSent': list(),
    'linkGrahStts': str,
    'linkGrahSpedFull': str,
    'linkGrahBitsRecd': str,
    'linkGrahBitsSent': str,
    'listIntcItem': list(),
    'listItemIDAdmnStts': list(),
    'listItemIDOperStts': list(),
    'listItemIDHighSped': list(),
    'listItemIDBitsRecd': list(),
    'listItemIDBitsSent': list(),
    'listIntcTrgr': list(),
    'listErrr': list()
}

patnDictZabxIntc = {
    'intc_A': str,
    'intc_B': str,
    'admnStts': str,
    'operStts': str,
    'highSped': 0,
    'bitsRecd': 0,
    'bitsSent': 0,
    'tredBitsRecdMax': 0,
    'tredBitsSentMax': 0,
    'itemIDAdmnStts': str,
    'itemIDOperStts': str,
    'itemIDHighSped': str,
    'itemIDBitsRecd': str,
    'itemIDBitsSent': str,
    'linkGrahStts': str,
    'linkGrahSped': str
}