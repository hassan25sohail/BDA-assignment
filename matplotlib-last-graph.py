import matplotlib.pyplot as plt

slice=[7,8,6,5]
label=["sleep","eat","work","play"]

plt.pie(slice,colors=["c","m","y","k"],labels=label)


plt.title("cool")

plt.legend()
plt.show()
