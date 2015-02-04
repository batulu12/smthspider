from word_processor2 import wordprocess,command

list = ['df','r','xyz','d','2','undo','test','redo','undo','undo'] #anwser ['df', 'r', 'xyz', 'test']
list2 = ['first', 'second', 'third','d','fourth','undo','undo','redo']
def test(list):
    wp = wordprocess()
    for item in list:
        if item == 'd':
            wp.del_com()
        elif item == 'undo':
            wp.undo_com()
        elif item == 'redo':
            wp.redo_com()
        else:
            wp.add_com(item)
        print wp.word_list
test(list2)