import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME= 2d46b6b4-cbf6-40eb-bbce-6251e6ba0300.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=32328;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=hqy66326;PWD=2q1ByYwhRO5Nx9In",'','')
print(conn)
print("connection successful...")