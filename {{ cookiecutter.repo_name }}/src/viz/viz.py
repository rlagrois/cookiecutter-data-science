
import itertools
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

def test():
    print("viz works!")

def plt_confusion(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.tight_layout()

def confusion(names,true,pred,
              title="Confusion Matrix",
              norm=False,prec=2,fig=True,show=True,
              cmap=plt.cm.Blues):
    cnf_matrix = confusion_matrix(true, pred)
    np.set_printoptions(precision=prec)
    if fig:
        plt.figure()
    plt_confusion(cnf_matrix, classes=names, normalize=norm, title=title,cmap=cmap)
    if show:
        plt.show()
    
    
def available():
    print('Available viz.viz Functions:')
    print('test() - tests if module is imported properly')
    print("plt_confusion(cm, classes, normalize=False, title='Confusion matrix', cmap=plt.cm.Blues) - confusion matrix")
    print("confusion(names,true,pred, title='Confusion Matrix', \n\tnorm=False,prec=2,fig=True,show=True,\n\tcmap=plt.cm.Blues) - creates and runs confusion matrix plotting")
