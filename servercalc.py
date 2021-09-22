from linmodel import LinModel
import phe as paillier
import json

def getData():
	with open('data.json', 'r') as file: 
		d=json.load(file)
	data=json.loads(d)
	return data

#getData()
def computeData():
	data=getData()
	mycoef=LinModel().getCoef()
	pk=data['public_key']
	pubkey= paillier.PaillierPublicKey(n=int(pk['n']))
	enc_nums_rec = [paillier.EncryptedNumber(pubkey, int(x[0], int(x[1]))) for x in data['values']]
	results=sum([mycoef[i]*enc_nums_rec[i] for i in range(len(mycoef))])
	return results, pubkey
#print(computeData())
def serializeData():
	results, pubkey = computeData()
	encrypted_data={}
	encrypted_data['pubkey'] = {'n': pubkey.n}
	encrypted_data['values'] = (str(results.ciphertext()), results.exponent)
	serialized = json.dumps(encrypted_data)
	return serialized
#print(serializeData())
data = age, he, al, gen =[24, 4, 6, 1]
mycoef = LinModel().getCoef()

#print(sum([data[i]*mycoef[i] for i in range(len(data))]))

def main():
	datafile=serializeData()
	with open('answer.json', 'w') as file:
		json.dump(datafile, file)

if __name__=='__main__':
	main()


