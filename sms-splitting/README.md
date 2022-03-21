Given an input string of arbitrary length, output SMS-compliant segments with suffixes.
A SMS-compliant segment is of length 160 characters or less.
Do not generate segments if the input fits in a single message.
A segment suffix looks like "(1/5)" for the first of five segments.
The segment content and suffix must both fit in the segment.
You must complete the function/method stub to return an array of message segments.
Input Constraints
Inputs will only consist of A-Z, a-z, spaces ( ), commas (,) and periods (.)
Your implementation can expect a maximum of 9 segments per input.
Extra Credit Case
The third test case has an additional output constraint: do not split words between segments! You should be able to iterate on your existing implementation.
Words will be delimited by a single space. Do not split on any other punctuation. You do not need to account for "unbreakable" i.e extremely long words in the input.
Spaces between words should be preserved in the first segment unless that violates the SMS length constraint, in which case the space should be included in the next segment.
For example, given the following text:
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus consequat nec dui quis maximus. Praesent vehicula feugiat condimentum. Nunc porta vulputate elit sit amet lacinia. Vivamus volutpat accumsan consequat. Nulla mattis odio erat, vel convallis neque semper nec. Integer a pharetra purus
The segment break would fall between "porta" and "volputate" with the space fitting in the first segment. The output would be:
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus consequat nec dui quis maximus. Praesent vehicula feugiat condimentum. Nunc porta (1/2) 
vulputate elit sit amet lacinia. Vivamus volutpat accumsan consequat. Nulla mattis odio erat, vel convallis neque semper nec. Integer a pharetra purus.(2/2)
However, if the text is modified slightly as follows:
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus consequat nec dui quis maximus. Praesent vehicula feugiat condimentum. Nunc portamludimi vulputate elit sit amet lacinia. Vivamus volutpat accumsan consequat. Nulla mattis odio erat, vel convallis neque semper nec. Integer a pharetra purus
Then the space should be placed in the beginning of the second segment:
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus consequat nec dui quis maximus. Praesent vehicula feugiat condimentum. Nunc portamludimi(1/2) 
 vulputate elit sit amet lacinia. Vivamus volutpat accumsan consequat. Nulla mattis odio erat, vel convallis neque semper nec. Integer a pharetra purus.(2/2)
Sample Test Case
Sample Input
Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis partu sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore ver rup. Li Europan lingues es membres del sam familie. Lor separat existentie es un myth. Por scientie, musica, sport etc, litot Europa.
Sample Output
Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis partu (1/3) sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore ver (2/3) rup. Li Europan lingues es membres del sam familie. Lor separat existentie es un myth. Por scientie, musica, sport etc, litot Europa.(3/3)