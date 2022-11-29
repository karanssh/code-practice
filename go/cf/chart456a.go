package main

import (
	"bytes"
	"fmt"
	"io"

	"github.com/wcharczuk/go-chart"
)

func chart456a(in io.Reader, out io.Writer) {

	graph := chart.Chart{
		Series: []chart.Series{
			chart.ContinuousSeries{
				XValues: []float64{1.0, 2.0, 3.0, 4.0},
				YValues: []float64{1.0, 2.0, 3.0, 4.0},
			},
		},
	}

	buffer := bytes.NewBuffer([]byte{})
	err := graph.Render(chart.PNG, buffer)
	fmt.Println(err)
}

// func main() { chart456a(os.Stdin, os.Stdout) }
