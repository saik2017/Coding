import matplotlib.pyplot as plt
mysample=[]
linear=[]
quadratic=[]
cubic=[]
exponential=[]
for i in range(30):
    mysample.append(i)
    linear.append(i)
    quadratic.append(i**2)
    cubic.append(i**3)
    exponential.append(1.5**i)

plt.figure('lin')
plt.xlabel("sample points")
plt.ylabel("linear function")
plt.title("Linear")
plt.plot(mysample,linear)
plt.figure('quad')
plt.plot(mysample,quadratic)
plt.figure("cubic")
plt.plot(mysample,cubic)
plt.figure("expo")
plt.plot(mysample,exponential)
plt.figure("cubic")
plt.show()
