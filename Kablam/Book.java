public class Book extends MediaItem {
     private String title,author;
     private double rating;

     public Book(){
          super("default title","default artist");
     }

     public Book(String title){
          this.title = title;
     }

     public Book(String title, String creator){
          super(title,creator);
     }

}
