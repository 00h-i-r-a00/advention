import pdb
import sys
from optparse import OptionParser
import os
	
def interaction():
	pass
	
def collect():
	pass

def analyze():
	pass

def report():
	pass

if __name__ == "__main__":
	
	parser = OptionParser()
	
	parser.add_option('-i', action='store_true', dest='interactive', help = 'Interactive Mode')
	parser.add_option('-c', action='store_true', dest='collect', help = 'Collection Mode')
	parser.add_option('-a', action='store_true', dest='analyze', help = 'Analysis Mode')
	parser.add_option('-r', action='store_true', dest='report', help = 'Reporter Mode')
	parser.add_option('-s', action='store_true', dest='single', help = 'Single Page Analysis Mode')
	parser.add_option('-b', action='store', type = 'string', dest='browser', help = 'Specifiy chrome, firefox or torbb')
	parser.add_option('-m', action='store', type = 'string', dest='method', help = 'Specifiy selenium or phantomjs')
	parser.add_option('-e', action='store', type = 'string', dest='extension', help = 'Specify httpseverywhere, adblockplus, both or none')
	
	(options, args) = parser.parse_args()

	if options.interactive:
		mode = 'interactive'
		mode_count += 1

	if options.analyze:
		mode = 'analyze'
		mode_count += 1
		
	if options.collect:
		mode = 'collect'
		mode_count += 1
		
	if options.single:
		mode = 'single'
		mode_count += 1
	
	if options.report:
		mode = 'report'
		mode_count += 1
		
	if len(options.browser) > 0:
		mode_count += 1
	
	if len(options.browser) == 0:
		print "Please enter which browser would you like to use: Firefox, Chrome or Tor Browser Bundle"
		sys.exit()
	
	if len(options.method) > 0:
		mode_count += 1
	
	if len(options.method) == 0:
		print "Please specify a crawling mechanism: selenium or phantomjs"	
	
	if len(options.extension) > 0:
		mode_count += 1
		
	if len(options.extension) == 0:
		print "Please specifiy an extension to use: httpseverywhere, adblockplus, both or none"
		sys.exit()
		
	if mode_count < 4:
		print('Error: Either one or more of these options missing: extension, method, browser')
		parser.print_help()
		exit()

	
	if mode == "interactive":
		print('\tWould you like to:')
		print('\t\t[C] Collect Data')
		print('\t\t[A] Analyze Data')
		print('\t\t[Q] Quit')
		
		while True:
			selection = input("\t Selection").lower()
			
			if selection == 'c':
				break
			if selection == 'q':
				sys.exit()
			else:
				print('\t\tValid selections are C, A, and Q.  Please try again.')
				continue
				
	
		if selection == 'c':
			##get the mechanism
			
			##if phantomjs:
				##create a phantomjs Class
				##run the function within the class (create a database)
				##also ask whether to ask to an existing file or create a new file
				##also add paralell processing
			
			
			##get the option for which browser and which extension
				##class for setting up the browser with or without an extension
			
			
			
	elif mode == "collect":
		pass
	elif mode == "analyze":
		pass
	elif mode == "single":
		pass
	elif mode == "report":
		pass
