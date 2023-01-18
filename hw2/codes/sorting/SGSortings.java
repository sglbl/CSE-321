import java.util.*;
/**
 * @author Solomon Golbol
   javac SGSortings.java && java SGSortings
 */
public class SGSortings{

    public static void main(String[] args) {
        ArrayList<String> lines = new ArrayList<>();
        lines.add("cahmet");
        lines.add("ahmet");
        lines.add("mehmet");
        lines.add("fehmet");
        lines.add("lehmet");
        lines.add("behmet");
        System.out.println("Unsorted -> " + lines.toString());
        //SGMergeSort(lines);
        // SGHeapSort(lines);
        SGQuicSort(lines, 0, lines.size()-1);
        System.out.println("Sorted   -> " + lines.toString());

    }
    
    public static void SGMergeSort(ArrayList<String> listToBeSort){
        if( listToBeSort.size() <= 1)
            return;
        
        ArrayList<String> leftTable;
        ArrayList<String> rightTable;

        int middle = listToBeSort.size() / 2;
        leftTable  = new ArrayList<String>();
        rightTable = new ArrayList<String>();
        for(int i=0; i<listToBeSort.size(); i++){
            if(i < middle) // it is odd number.
                leftTable.add(  listToBeSort.get(i) );
            else
                rightTable.add( listToBeSort.get(i) );
        }

        SGMergeSort(leftTable);
        SGMergeSort(rightTable);

        merge(leftTable, rightTable, listToBeSort);
    }

    private static void merge(ArrayList<String> leftTable, ArrayList<String> rightTable, ArrayList<String> realTable) {
        int index, leftIndex, rightIndex;
        index = 0;
        leftIndex = 0;
        rightIndex = 0;
        while(leftIndex < leftTable.size() && rightIndex < rightTable.size()){
            if( leftTable.get(leftIndex).compareTo(rightTable.get(rightIndex)) < 0 ){
                realTable.set(index, leftTable.get(leftIndex));
                leftIndex++;
                index++;
            }
            else{
                realTable.set(index, rightTable.get(rightIndex));
                rightIndex++;
                index++;
            }
        }

        while( leftIndex < leftTable.size() ){
            realTable.set(index, leftTable.get(leftIndex) );
            leftIndex++;
            index++;
        } 

        while( rightIndex < rightTable.size() ){
            realTable.set(index, rightTable.get(rightIndex) );
            rightIndex++;
            index++;
        }

    }

    /** ##################################################################### */
    
    public static void SGHeapSort(ArrayList<String> heap){
        for(int i= heap.size() /2; i>=0; i--)
            heapify(heap, i, heap.size());

        //Moving current index (root) to end of heap.
        for(int i=heap.size()-1; i>0; i--){
            // Changing heap values top and 
            String temp = heap.get(0);
            heap.set(0, heap.get(i) );
            heap.set(i, temp);
            
            heapify(heap, 0, i);
        }
        
    }

    /**
     * Fixes the heap
     */
    public static void heapify(ArrayList<String> heap, int index, int size){
        int leftIndex, rightIndex;
        
        while(true){
            leftIndex  = 2*index+1;
            rightIndex = 2*index+2;
            if(leftIndex >= size)
                break;
            int biggestChild;
            if(rightIndex >= size || heap.get(leftIndex).compareTo( heap.get(rightIndex) ) >= 0 ) 
                biggestChild = leftIndex;
            else
                biggestChild = rightIndex;
            if(heap.get(biggestChild).compareTo(heap.get(index)) <= 0)
                break;
            
            String temp = heap.get(index);
            heap.set(index, heap.get(biggestChild) );
            heap.set(biggestChild, temp);
            index = biggestChild;
        }
    }

    /** ##################################################################### */
    
    public static void SGQuicSort(ArrayList<String> lines, int firstIndex, int lastIndex ){
        int partit;
        if(firstIndex < lastIndex){
            partit = partition(lines, firstIndex, lastIndex);
            int leftSide = partit-1;
            SGQuicSort(lines, firstIndex, leftSide);
            int rightSide = partit+1;
            SGQuicSort(lines, rightSide, lastIndex);
        }
    }

    private static int partition(ArrayList<String> lines, int firstIndex, int lastIndex) {
        String pivot; 
        int down = firstIndex-1;

        //Starting pivot from last index of partition.
        pivot = lines.get(lastIndex);
        //System.out.println("Pivot is " + pivot);
        
        int counter = firstIndex;
        while(counter <= lastIndex-1){ //In a loop checking every element with pivot value.
            if(lines.get(counter).compareTo(pivot) < 0){
                down++;
                //swapping
                String temp = lines.get(down);
                lines.set(down, lines.get(counter));
                lines.set(counter, temp);
            }
            counter++;
        }

        int returnValue;
        returnValue = down+1;
        //Swapping 
        String temp = lines.get(returnValue);
        lines.set(returnValue, lines.get(lastIndex) );
        lines.set(lastIndex, temp);

        return returnValue;
    }


}