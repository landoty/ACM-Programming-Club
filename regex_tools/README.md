# Grep and Awk - Unix Regular Expression Tools
### ACM Programming Club 02-16-22

## What is Grep and Awk
- **Grep** : Global Regular Expression Print
	- Unix command-line utility for searching plaintext files that match a certain regular expression
	- Can be partnered with other Unix commands (ls, cat, etc.) for expanded functionality

- **Awk** : Scripting language created by Aho, Weinberger, and Kernighan
	- Unix-driven scripting language used for text processing
	- Powerful one-liners, but is Turing complete
	- Supports the string, integer, associate array types and regular expressions

## Why learn these?
- Consider the following problem: 
	- The file data/apache\_log contains a portion of an Apache web server log. The IT security team discovered a breach in the companies private 91.0.0.0/8 IP range. Find all requests by these IP addresses and the resources they requested
- A multipurpose programming language **can** solve this problem, but can be done much simpler using grep, awk, and/or other Unix utilities

## Starting Simple : Grep
- **usage**: grep [-options] "\<pattern\>" \<file name|>
- **pattern**: must be a regular expression (typically just a string)
- **useful options**:
	- **-n**: include line number
	- **-v**: "negative results"
	- **-l**: lists only the file name with matching pattern
	- **-o**: only print the matched pattern
	- **-i**: ignore case
	- **-x**: exact match to the pattern

**See more in the grep manual page**

## Expanding grep
- Grep is great at gaining insight on what a file contains, but is fairly limited beyond that
- Combine other linux utilities for expanded functionality
	- **pipe |**: use output of preceding command as the input of the following
	- **sort**
	- **uniq**
	- **>** : direct output into a file

## Introducing AWK
- Awk is procedural scripting language that processes data using a line-by-line approach
- All awk programs follow the format:

**BEGIN**{commands} /pattern/{commands} **END**{commands}

### Running AWK programs
Awk programs can be ran either in line or via an awk script
- **In line** : awk [-options] 'BEGIN{}...END{}' \<file name\>
- **Script**: awk [-options] script.awk \<file name\>

### AWK Basics
- Awk sees each line as number of fields, each seperated by a field seperator FS
- Each field can be accessed directly using the **$** operator
	- Use the line "we are learning awk"
	- **$0** represents the entire line
	- **$1** = "we"
	- **$NF** (number of fields, i.e the last line) = awk
- The patterns preceding the line commands can be combined with regular expressions and logical symbols
- Awk also has support for other common operators (arithmetic, unary, etc) as seen in other languages

### AWK Regular Expressions and Patterns
- **Single character** : dot operator .
- **Start of a line or field** : ^
- **End of a line or field** : $
- **Character set** : []
- **None or one** : ?
- **None or many** : Kleene star *
- **One or many** : Kleene plus +
- **Union/OR** : |

### Arrays in AWK 
- Awk uses associative arrays and can be indexed via a string OR an integer
- **Create an array by adding an element**
	- array["element1"] = "first"
- **Append by indexing with non-existent element**
	- array["element2"] = "second"

### Disclaimer
This information is all we have time for within the hour of programming club. If you wish to learn more on
awk - of which there is much to learn - please visit the [gnu documentation]("https://www.gnu.org/software/gawk/manual/gawk.html")
