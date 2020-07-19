import java.util.*;

class Main

{

  public static void main(String[] args)

  {

    Scanner sc=new Scanner(System.in);

    int t=sc.nextInt();

    while(t>0)

    {

      t--;

      int n=sc.nextInt();

      int[] a=new int[n];

      for(int i=0;i<n;i++)

        a[i]=sc.nextInt();

      int res=0;

      /*for(int i=0;i<n-2;i++)

      {

        int max=a[i+1],min=a[i+1],count=0;

        for(int j=i+1;j<n;j++)

        {

          /*for(int k=j+1;k<n;k++)

          {

            if(a[i]<a[j] && a[j]<a[k])

            {

              max=Math.max(max,a[i]-a[j]+a[k]);

            }

          }

          if(a[j]>a[i])

          {

            count++;

            if(a[j]>max)

              max=a[j];

            if(a[j]<min)

              min=a[j];

          }

        }

        if(count<2)

          continue;

        res=Math.max(res,a[i]-min+max);

      }

      System.out.println(res);*/

      int[] left=new int[n];

      int[] right=new int[n];

      int max=a[n-1];

      for(int i=n-2;i>=0;i--)

      {

        if(max>a[i])

         right[i]=max;

        else right[i]=-1;

        if(a[i]>max)

        {

          max=a[i];

        }

      }

      /*for(int i=1;i<n;i++)

      {

        max=Integer.MIN_VALUE;

        for(int j=0;j<i;j++)

        {

          if(a[j]<a[i] && a[j]>max)

            max=a[j];

        }

        if(max==Integer.MIN_VALUE)

          left[i]=-1;

        else left[i]=max;

      }*/

      TreeSet<Integer> set = new TreeSet<>();

      for(int i=1;i<n;i++)

      {

        set.add(a[i-1]);

        Integer result=set.lower(a[i]);

        if(result!=null)

          left[i]=result;

        else left[i]=-1;

      }

      for(int i=1;i<n-1;i++)

      {

        if(left[i]!=-1 && right[i]!=-1)

        res=Math.max(res,left[i]-a[i]+right[i]);

      }

      System.out.println(res);

    }

  }

}
