package main

import (
	"io"
)

func jsonParserTestSetValNested(in io.Reader, out io.Writer) {
	// keysList := []string{"ipv4", "source", "address", "group"}
	// setVal := []byte(`"KaranTest"`)
	// outputVal, err := jsonparser.Set([]byte(buggedString), setVal, keysList...)
	// fmt.Println(string(outputVal), err)
}

// func main() { jsonParserTestSetValNested(os.Stdin, os.Stdout) }

const (
	buggedString = `
	{
		
			  "ipv4":{
				 "name":"testDependency",
				 "source":{
					"address":{
					   "group":"testDepenffdency",
					   "ff":"aa"
					},
					"port":{
					   "any":true
					}
				 },
				 "uuid":"653e5654-b56b-47c1-b4e5-206acbb28f7a"
			  }
	 }
	 
	 `
	expectedString = `
	 {

		"ipv4":{
			   "name":"testDependency",
			   "source":{
					  "address":{
						 "group":"KaranTest",
						 "ff":"aa"
					  },
					  "port":{
						 "any":true
					  }
			   },
			   "uuid":"653e5654-b56b-47c1-b4e5-206acbb28f7a"
		}
}
	 `
	gotString = `
	 {

		"ipv4":{
			   "name":"testDependency",
			   "source":{
					  "address":{
						 "group":KaranTest,
						 "ff":"aa"
					  },
					  "port":{
						 "any":true
					  }
			   },
			   "uuid":"653e5654-b56b-47c1-b4e5-206acbb28f7a"
		}
}
`
)
