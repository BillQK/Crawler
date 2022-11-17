High Level Approach:
In order to complete this assignment, we implemented a form of Depth First Search to crawl through the all the links of the server and keep track of what we have done. To achieve this goal, we first had methods that would automate sending get requests, and build sockets to get the HTTP responses. Then after implementing those methods we had another method log in method that would send the correct post request with the information specified through the command line to the server and continue through to the actual website to crawl.

After logging into the server, we then implmented DFS since the links are connected graph, by putting the inital links seen when you first log in, into a queue list, and then popping the first item if it recieved a HTTP response. With each page, we check to see if there is a flag on that page to print, and then we go through all that persons friend links, and if the page had not been visited before, we add that to the queue, and then we continue that until we have found all 5 flags then we can return or in the worse case, go thorugh all the links in our queue.

Challenges Faced:
Correctly exploring all the friend pages for a user, at times due to the HTML parser list we had, some items would remain in the list that we had already seen, and would either cause unnecessary page calls, or sometimes break out of going through all the pages prematurely

Understanding HTMl and HTML parser, and knowing how to find the specific data that we need such as href tags, or the flag data

Properly recieving all the data coming in through the socket since at times all the data wouldn't come through the buffer limit we set

Reverse enginering the POST request.

Overview of how we tested our code.
Before we implented our DFS on the entire website, we started small with processing only 2-3 persons at first, and having print statements within our code to check to make sure the crawler had accessed all of persons friend pages by printing out the current page it was crawling, furthemore we had counts to make sure that the crawler was going through as many pages as expected.
Furthermore, we also testing our program on the Khoury machines to make sure the program still functioned fine and found all the flags.

