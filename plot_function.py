from matplotlib import pyplot as plt

def bar_scatter_plot(datos):
    datos.sort_values('Library_Holdings', inplace=True)
    datos.reset_index(inplace=True)
    fig, ax = plt.subplots(figsize=(20,10), dpi= 100)
    ax.vlines(x=datos.index, ymin=0, ymax=datos.Library_Holdings)
    ax.scatter(x=datos.index, y=datos.Library_Holdings)
    # Title, Label, Ticks and Ylim
    ax.set_title("Authors' ranking by library holdings", fontdict={'size':22})
    ax.set_ylabel('Library holdings', fontdict={'size':16})
    ax.set_xlabel('Authors', fontdict={'size':16})
    ax.set_xticks(datos.index)
    ax.set_xticklabels(datos.Worldcat_entity, rotation=45, fontdict={'horizontalalignment': 'right', 'size':12})
    ax.set_ylim(0, max(datos.Library_Holdings)+200)

    # Annotate
    for row in datos.itertuples():
        ax.text(row.Index, row.Library_Holdings+50, s=row.Library_Holdings,
                horizontalalignment= 'center',
                verticalalignment='bottom',
                fontsize=10)