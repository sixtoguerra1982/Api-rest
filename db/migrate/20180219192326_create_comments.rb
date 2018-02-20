class CreateComments < ActiveRecord::Migration[5.1]
  def change
    create_table :comments do |t|
      t.integer :user_id
      t.text :content
    end
    add_reference :comments, :feed, index: true
  end
end
