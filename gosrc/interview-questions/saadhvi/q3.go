package main

import "fmt"

//import "fmt"
/*

Scientists have discovered a species of fire-breathing dragons. DNA analysis of the dragon reveals that it is a reptile evolved from a common ancestor of crocodile,

hundreds of millions of years ago. Even though they're related, the different reptile species cannot cross-breed.

Researchers would like to develop a lifecycle model of this rare species, in order to better study them. Complete the implementation below so that:

The FireDragon species implements the Reptile interface.
When a ReptileEgg hatches, a new reptile will be created of the same species that laid the egg.
nil is returned if a ReptileEgg tries to hatch more than once.
*/
type Reptile interface {
	Lay() ReptileEgg
	New() Reptile
}

type ReptileEgg struct {
	Hatched bool
	Parent  Reptile
}

func (egg *ReptileEgg) Hatch() Reptile {
	if egg.Hatched {
		return nil
	}
	egg.Hatched = true
	return egg.Parent.New()
}

type FireDragon struct {
	Name string
}

func (f *FireDragon) Lay() ReptileEgg {
	return ReptileEgg{
		Parent: f,
	}
}

func (f *FireDragon) New() Reptile {
	return &FireDragon{
		Name: "Child",
	}
}

func main() {
	var fireDragon = FireDragon{Name: "Parent"}
	fmt.Println(fireDragon)
	var egg ReptileEgg = fireDragon.Lay()
	var childDragon Reptile = egg.Hatch()
	fmt.Println(fireDragon, egg, childDragon, egg.Hatch())
}
