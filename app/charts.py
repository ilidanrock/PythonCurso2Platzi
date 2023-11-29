import matplotlib.pyplot as plt

def generate_plot(labels, values):


    fig , ax = plt.subplots()
    ax.bar(labels, values)

    plt.show()

def generate_pie(labels, values):
  
    fig , ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

if __name__ == '__main__':
    labels = ['A', 'B', 'C']
    values = [1, 4, 2]
    generate_plot( labels, values )
    generate_pie( labels, values )