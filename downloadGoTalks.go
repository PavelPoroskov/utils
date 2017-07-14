package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"log"
	"net/http"
	"path/filepath"
	s "strings"
	html "golang.org/x/net/html"
//	"strconv"
)

var outFolder string

func DownloadFile( pathBase, pathSub string, iLevel int ) {

	fullpath := pathBase + pathSub
	res, err := http.Get( fullpath )
	if err != nil {
		log.Fatal(err)
	}

	bytesTxt, err := ioutil.ReadAll(res.Body)
	res.Body.Close()
	if err != nil {
		log.Fatal(err)
	}

//	fmt.Println("pathSub: " + pathSub + " " + strconv.Itoa(iLevel) )

	fileName := pathSub[1:]
	if iLevel < 2 {
		fileName = s.Replace( fileName, "/", "__", -1 )
//	}else{
//
	}

	doString := false
	var stringTxt string
	if s.HasSuffix(fileName,".slide") {
		fileName = fileName + ".html"		
		//body style="display: none" --+ body
		//styles.css --+ styles0.css

//		stringTxt = bytesTxt.String() //-
//		stringTxt = String(bytesTxt) //-
//		stringTxt = fmt.Sprintf("%s", bytesTxt) //+
		stringTxt = string(bytesTxt)
		stringTxt = s.Replace( stringTxt, "body style=\"display: none\"", "body", -1 )
		stringTxt = s.Replace( stringTxt, "body style='display: none'", "body", -1 )
		stringTxt = s.Replace( stringTxt, "styles.css", "styles0.css", -1 )
		doString = true
	} else if s.HasSuffix(fileName,".article") {
		fileName = fileName + ".html"		
	}

	if s.HasSuffix(fileName,".html") {
	  if doString {

	 	}else{
			stringTxt = string(bytesTxt)
			doString = true
	 	}

		arNamesU := s.Split(pathSub,"/")
		arNamesU = arNamesU[:len(arNamesU)-1]
		sumBaseURL := pathBase
		for _, sName := range arNamesU {
			sumBaseURL = sumBaseURL + "/" + sName
		}
		sumBaseURL = sumBaseURL + "/"
	 	
		stringTxt = s.Replace( stringTxt, "img src=\"", "img src=\"" + sumBaseURL, -1 )
	}


//	fileName = outFolder + "\\" + fileName
	arNames := s.Split(fileName,"/") 
	sumPath := outFolder
//	sumDir := outFolder
	for _, sName := range arNames {
		sumPath = filepath.Join( sumPath, sName )
//		sumDir = filepath.Join( sumPath, sName )
	}
	fileName = sumPath

	sDir, _ := filepath.Split(fileName)
	if _, errD := os.Stat(sDir); os.IsNotExist(errD) {
		os.MkdirAll( sDir, os.ModePerm )
	}

	f, errf := os.Create(fileName)
	if errf != nil {
      panic(errf)
  }
  if doString {
    f.WriteString(stringTxt)
 	}else{
    f.Write(bytesTxt)
 	}
  f.Sync()
  f.Close()

//  panic("end pp")
}

func doSubDir( pathBase, pathSub string, iLevel int ) {

	fullpath := pathBase + pathSub
	res, err := http.Get( fullpath )
	if err != nil {
		log.Fatal(err)
	}
//  sSite := res.Request.URL.String()
//  fmt.Println("Year: " + sSite)

	doc, err := html.Parse(res.Body)
	if err != nil {
	    log.Fatal(err)
	}

	
	var f func(*html.Node, bool) bool
	f = func(n *html.Node, inHaveSubFolder bool) bool {
	    resHaveSubFolder := inHaveSubFolder

	    if n.Type == html.ElementNode {
	    	if n.Data == "a" {
	        for _, a := range n.Attr {
	            if a.Key == "href" {
	                if !(a.Val == "/" || s.HasPrefix(a.Val,"http") ) {
//		                doYear( sSite + a.Val )
//	                	sPref := s.Repeat( "--", iLevel )
	                	sPref := ""
		                if inHaveSubFolder {
		                	sPref = sPref + "d-"
			                fmt.Println( sPref + a.Val )
			                doSubDir(pathBase, a.Val, iLevel + 1 )
		                } else {
		                	sPref = sPref + "--"
			                fmt.Println( sPref + a.Val )
//			                DownloadFile( pathBase, a.Val, iLevel + 1 )
			                DownloadFile( pathBase, a.Val, iLevel )
		                }
	                }
	                break
	            }
	        }
	      } else if n.Data == "h4" && n.FirstChild.Data== "Sub-directories:"{
//            fmt.Println("--Sub-directories:")
            resHaveSubFolder = true
	      }
	    }

	    siblHaveSubFolder := inHaveSubFolder
	    for c := n.FirstChild; c != nil; c = c.NextSibling {
	        siblHaveSubFolder = f( c, siblHaveSubFolder )
	    }

	    return resHaveSubFolder
	}
	f(doc,false)	
}

func main() {

	outFolder = "D:\\_bin\\Go.talks"

	doSubDir( "https://talks.golang.org", "", 0 )
//	doSubDir( "https://talks.golang.org", "/2012", 0 )
}