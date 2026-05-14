import mpi.MPI;

public class ArraySumMPI {

    public static void main(String[] args) throws Exception {

        MPI.Init(args);

        int rank = MPI.COMM_WORLD.Rank();
        int size = MPI.COMM_WORLD.Size();

        int[] array = {1,2,3,4,5,6,7,8,9,10};

        int n = array.length;

        int localSum = 0;

        int startIndex = rank * (n / size);

        int endIndex = (rank == size - 1)
                ? (n - 1)
                : (startIndex + (n / size) - 1);

        for(int i = startIndex; i <= endIndex; i++) {
            localSum += array[i];
        }

        int[] sendbuf = {localSum};
        int[] recvbuf = {0};

        MPI.COMM_WORLD.Reduce(
                sendbuf,
                0,
                recvbuf,
                0,
                1,
                MPI.INT,
                MPI.SUM,
                0
        );

        if(rank == 0) {
            System.out.println("Global sum: " + recvbuf[0]);
        }

        MPI.Finalize();
    }
}