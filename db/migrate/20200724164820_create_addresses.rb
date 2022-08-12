class CreateAddresses < ActiveRecord::Migration[5.2]
  def change
    create_table :addresses do |t|
      t.string :addressable_type
      t.integer :addressable_id
      t.string :street
      t.string :number
      t.string :zip_code
      t.string :neighborhood
      t.string :city
      t.string :state

      t.timestamps null: false
    end
  end
end
